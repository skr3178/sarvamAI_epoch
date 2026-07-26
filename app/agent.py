"""Multi-turn intake agent.

Latency shape matters here: a Sarvam chat call costs ~20s, but a patient must not wait
20s to be answered. So the conversational path is instant (STT -> deterministic red-flag
check -> pre-translated question -> TTS ~3s) while note structuring runs in a background
thread and lands on the doctor screen as it completes. The model's own proposed follow-up
is used from turn 2 onward whenever the background call has finished in time.
"""
import json
import re
import threading
import time
import uuid
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import redflags, sarvam_client as sv
from .pipeline import DOCTOR_ROSTER, FORBIDDEN_PATIENT_FACING, book

DATA_DIR = Path(__file__).resolve().parent / "data"
AUDIO_DIR = DATA_DIR / "audio"
MAX_PATIENT_TURNS = 3
STRUCTURE_WAIT_S = 30  # only waited for on the final turn, before booking

_pool = ThreadPoolExecutor(max_workers=4)
_jobs: dict[str, object] = {}   # session id -> Future of the latest structuring call
_locks: dict[str, threading.Lock] = {}

STRUCTURE_PROMPT = """Extract clinic intake JSON. No prose. Never diagnose.

Patient said (in order):
{HISTORY}

Rules: on self-correction the LAST value wins, and log it in corrections.
confidence is 0-1 per field. areas_to_consider = symptom areas a clinician might explore, never a diagnosis.
follow_up_question: the single most useful next question in English, non-leading, or null if nothing important is missing.

{"chief_complaint":"","symptoms":[],"onset_duration":"","corrections":[{"field":"","old":"","new":""}],"severity_words":null,"medications_mentioned":[],"age":null,"confidence":{"chief_complaint":0,"onset_duration":0,"age":0},"category":"fever|stomach|general|weakness|infection|joint|bone|back|injury|ear|throat|nose|cough","areas_to_consider":[],"follow_up_question":""}"""

VALID_CATEGORIES = {c for d in DOCTOR_ROSTER for c in d["categories"]}

# Deterministic question ladder. Pre-translated so a follow-up costs no model call.
QUESTION_LADDER = [
    ("chief_complaint", "What is troubling you the most right now?",
     "अभी आपको सबसे ज़्यादा क्या तकलीफ़ हो रही है?"),
    ("onset_duration", "Since when has this been going on?",
     "यह तकलीफ़ कब से है?"),
    ("severity_words", "How bad is it — is it stopping you from doing your daily work?",
     "तकलीफ़ कितनी है — क्या इससे आपका रोज़ का काम रुक रहा है?"),
    ("associated", "Is there anything else along with it?",
     "इसके साथ और कुछ भी हो रहा है — बुखार, उल्टी, या कहीं और दर्द?"),
]

ESCALATION_HI = "यह ज़रूरी है — मैं अभी स्टाफ़ को बुला रही हूँ। कृपया वहीं रहिए।"
GARBLED_HI = "माफ़ कीजिए, आवाज़ साफ़ नहीं आई। कृपया फिर से बताइए।"


def _session_file(sid: str) -> Path:
    return DATA_DIR / f"session_{sid}.json"


def new_session(phone: str | None = None) -> dict:
    sid = uuid.uuid4().hex[:8]
    state = {
        "id": sid, "phone": phone, "created": time.time(), "turns": [],
        "note": {}, "status": "open", "booking": None, "red_flags": [],
        "asked": [], "structuring": False,
    }
    _locks[sid] = threading.Lock()
    save(state)
    return state


def save(state: dict) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    _session_file(state["id"]).write_text(json.dumps(state, ensure_ascii=False, indent=1))


def load(sid: str) -> dict:
    return json.loads(_session_file(sid).read_text())


def safety_filter(text: str) -> str:
    """Patient-facing text may never contain diagnosis/advice language (code-level boundary)."""
    if FORBIDDEN_PATIENT_FACING.search(text):
        return "आपकी बात नोट कर ली गई है। डॉक्टर आपसे जल्द मिलेंगे।"
    return text


def _clean_category(value) -> str:
    """The model sometimes echoes the enum ('fever|stomach'); take the first valid token."""
    for token in re.split(r"[|,/]", str(value or "")):
        token = token.strip().lower()
        if token in VALID_CATEGORIES:
            return token
    return "general"


def _structure(sid: str, history: str) -> dict:
    """Background call: turn the conversation so far into the structured note."""
    note = sv.chat_json([{"role": "user",
                          "content": STRUCTURE_PROMPT.replace("{HISTORY}", history)}])
    note["category"] = _clean_category(note.get("category"))
    if isinstance(note.get("corrections"), list):
        note["corrections"] = [c for c in note["corrections"] if isinstance(c, dict) and c.get("new")]
    with _locks.setdefault(sid, threading.Lock()):
        state = load(sid)
        proposed = note.pop("follow_up_question", None)
        state["note"] = note
        state["proposed_question"] = proposed
        state["structuring"] = False
        save(state)
    return note


def _kick_off_structuring(state: dict) -> None:
    history = "\n".join(f"{t['n']}. {t['english']}" for t in state["turns"])
    state["structuring"] = True
    save(state)
    _jobs[state["id"]] = _pool.submit(_structure, state["id"], history)


# Instant gap detection straight off the transcript, so turn 1 asks a sensible question
# before the ~20s structuring call has returned anything.
_HAS_DURATION = re.compile(
    r"\b(day|days|week|weeks|month|months|year|years|hour|hours|night|morning|yesterday|"
    r"since|from last|for the last|today)\b", re.I)
_HAS_SEVERITY = re.compile(
    r"\b(severe|severely|mild|slight|bad|worse|worst|little|bit|lot|unbearable|"
    r"can'?t|cannot|unable|heavy|light|terrible|intense)\b", re.I)


def _covered(state: dict) -> set[str]:
    """Fields already covered, from the structured note or the raw transcripts."""
    note, said = state["note"], " ".join(t["english"] for t in state["turns"])
    covered = {f for f in ("chief_complaint", "onset_duration", "severity_words") if note.get(f)}
    if len(said.split()) >= 4:
        covered.add("chief_complaint")
    if _HAS_DURATION.search(said):
        covered.add("onset_duration")
    if _HAS_SEVERITY.search(said):
        covered.add("severity_words")
    return covered


def _next_question(state: dict) -> tuple[str, str] | None:
    """(english, hindi) of the next question, or None if we have enough to book."""
    note = state["note"]
    asked = state["asked"]
    covered = _covered(state)
    proposed = state.get("proposed_question")
    for field, english, hindi in QUESTION_LADDER:
        if field in asked:
            continue
        if field == "associated":
            continue  # only used as a filler when the ladder is otherwise satisfied
        if field not in covered:
            # Prefer the model's own question once structuring has produced one.
            if proposed and len(state["turns"]) > 1:
                return proposed, _to_hindi(proposed)
            return english, hindi
    if len(state["turns"]) < 2 and "associated" not in asked:
        field, english, hindi = QUESTION_LADDER[-1]
        if proposed:
            return proposed, _to_hindi(proposed)
        return english, hindi
    return None


def _to_hindi(question: str) -> str:
    for _, english, hindi in QUESTION_LADDER:
        if question.strip() == english:
            return hindi
    try:
        return sv.chat_json([{"role": "user", "content":
            "Translate to natural spoken Hindi (Devanagari). JSON only: "
            '{"hi":"..."}\nText: ' + question}])["hi"]
    except Exception:
        return "थोड़ा और बताइए।"


def _field_for(question: str) -> str:
    for field, english, _ in QUESTION_LADDER:
        if question.strip() == english:
            return field
    return "model_proposed"


def process_turn(state: dict, audio_path: str) -> dict:
    """One patient utterance -> updated state + spoken reply."""
    stt = sv.stt_translate(audio_path)
    english = (stt.get("transcript") or "").strip()
    lang = stt.get("language_code") or "hi-IN"

    if not english:
        return _reply(state, GARBLED_HI, done=False)

    state["turns"].append({
        "n": len(state["turns"]) + 1, "audio": Path(audio_path).name,
        "english": english, "language": lang, "ts": time.time(),
    })

    # Deterministic red-flag check, before any model call, on every turn.
    flags = redflags.check(english)
    if flags:
        state["red_flags"] = flags
        state["status"] = "escalated"
        state["booking"] = book("urgent", urgent=True)
        save(state)
        _kick_off_structuring(load(state["id"]))  # note still assembles for the doctor
        return _reply(state, ESCALATION_HI, done=True)

    _kick_off_structuring(state)

    # Merge in whatever background structuring has already finished.
    state = load(state["id"])
    question = _next_question(state) if len(state["turns"]) < MAX_PATIENT_TURNS else None

    if question:
        english_q, hindi_q = question
        state["asked"].append(_field_for(english_q))
        save(state)
        return _reply(state, safety_filter(hindi_q), done=False)

    # Booking: use the category already structured from earlier turns so the patient hears
    # the confirmation immediately. Only block if nothing has been structured at all yet.
    if not state["note"].get("category"):
        job = _jobs.get(state["id"])
        if job is not None:
            try:
                job.result(timeout=STRUCTURE_WAIT_S)
            except Exception:
                pass
        state = load(state["id"])
    booking = book(state["note"].get("category", "general"), urgent=False)
    state["booking"] = booking
    state["status"] = "booked"
    save(state)
    reply = safety_filter(
        f"आपकी बात नोट हो गई है। {booking['doctor']} से {booking['slot']} बजे "
        "अपॉइंटमेंट बुक हो गया है। जल्दी स्वस्थ होइए।")
    return _reply(state, reply, done=True)


def _reply(state: dict, reply_text: str, done: bool) -> dict:
    audio = sv.tts(reply_text, language_code="hi-IN")
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    fname = f"reply_{state['id']}_{len(state['turns'])}_{int(time.time())}.wav"
    (AUDIO_DIR / fname).write_bytes(audio)
    return {
        "session": state, "reply_text": reply_text,
        "reply_audio": f"/audio/{fname}", "done": done,
    }

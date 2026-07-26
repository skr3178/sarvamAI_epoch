"""Multi-turn intake agent: session state, follow-up engine, booking, safety boundary."""
import json
import time
import uuid
from pathlib import Path

from . import redflags, sarvam_client as sv
from .pipeline import DOCTOR_ROSTER, FORBIDDEN_PATIENT_FACING, book

DATA_DIR = Path(__file__).resolve().parent / "data"
AUDIO_DIR = DATA_DIR / "audio"
MAX_PATIENT_TURNS = 3

STRUCTURE_PROMPT = """Clinic intake structurer. Never diagnose. Output JSON only, no prose.

Patient statements (English), in order:
{HISTORY}

Existing note: {NOTE}

Rules: last stated value wins on self-corrections, and log the correction. confidence 0-1 per field.
Ask a follow_up only if chief_complaint, onset_duration or severity is still missing; else null.

JSON:
{"chief_complaint":"","symptoms":[],"onset_duration":"","corrections":[{"field":"","old":"","new":""}],"severity_words":null,"medications_mentioned":[],"age":null,"confidence":{"chief_complaint":0,"onset_duration":0,"age":0},"category":"fever|stomach|general|weakness|infection|joint|bone|back|injury|ear|throat|nose|cough","areas_to_consider":[],"follow_up_question":null}"""

REPLY_PROMPT = """Clinic receptionist speaking to a patient in Hindi (Devanagari). Never give medical opinion, advice or reassurance about the illness.

You understood: {SUMMARY}
{CORRECTION}
Next question to ask: {QUESTION}

Write ONE or TWO short spoken sentences: briefly confirm back what you understood (mention the corrected value if there was a correction), then ask the question. Output only the Hindi sentence(s), nothing else."""


VALID_CATEGORIES = {c for d in DOCTOR_ROSTER for c in d["categories"]}

# The required-field ladder: the job is not capturable until these exist.
GENERIC_QUESTIONS = {
    "chief_complaint": "What is troubling you the most right now?",
    "onset_duration": "Since when has this been going on?",
    "severity_words": "How bad is it — is it stopping you from doing your daily work?",
}


def _clean_category(value) -> str:
    """The model sometimes echoes the enum ('fever|stomach'); take the first valid token."""
    for token in str(value or "").replace(",", "|").split("|"):
        token = token.strip().lower()
        if token in VALID_CATEGORIES:
            return token
    return "general"


def _missing_field(note: dict) -> str | None:
    for field in ("chief_complaint", "onset_duration", "severity_words"):
        if not note.get(field):
            return field
    return None


def _session_file(sid: str) -> Path:
    return DATA_DIR / f"session_{sid}.json"


def new_session(phone: str | None = None) -> dict:
    sid = uuid.uuid4().hex[:8]
    state = {
        "id": sid, "phone": phone, "created": time.time(), "turns": [],
        "note": {}, "status": "open", "booking": None, "red_flags": [],
    }
    save(state)
    return state


def save(state: dict) -> None:
    DATA_DIR.mkdir(exist_ok=True)
    _session_file(state["id"]).write_text(json.dumps(state, ensure_ascii=False, indent=1))


def load(sid: str) -> dict:
    return json.loads(_session_file(sid).read_text())


def safety_filter(text: str) -> str:
    """Patient-facing text must never contain diagnosis/advice language (code-level boundary)."""
    if FORBIDDEN_PATIENT_FACING.search(text):
        return "आपकी बात नोट कर ली गई है। डॉक्टर आपसे जल्द मिलेंगे।"
    return text


def process_turn(state: dict, audio_path: str) -> dict:
    """One patient utterance -> updated state + spoken reply. Returns the reply payload."""
    stt = sv.stt_translate(audio_path)
    english = (stt.get("transcript") or "").strip()
    lang = stt.get("language_code") or "hi-IN"

    turn = {
        "n": len(state["turns"]) + 1, "audio": Path(audio_path).name,
        "english": english, "language": lang, "ts": time.time(),
    }
    state["turns"].append(turn)

    if not english:
        reply = "माफ़ कीजिए, आवाज़ साफ़ नहीं आई। कृपया फिर से बताइए।"
        state["turns"].pop()  # garbled turn doesn't count against the limit
        save(state)
        return _reply(state, reply, done=False)

    # Deterministic red-flag check BEFORE any LLM call, every turn.
    flags = redflags.check(english)
    if flags:
        state["red_flags"] = flags
        state["status"] = "escalated"
        state["booking"] = book("urgent", urgent=True)
        state["note"].setdefault("verbatim_statements", []).append(english)
        save(state)
        reply = "यह ज़रूरी है — मैं अभी स्टाफ को बुला रही हूँ। कृपया वहीं रहिए।"
        return _reply(state, reply, done=True)

    history = "\n".join(f"{t['n']}. {t['english']}" for t in state["turns"])
    prompt = (STRUCTURE_PROMPT
              .replace("{HISTORY}", history)
              .replace("{NOTE}", json.dumps(state["note"], ensure_ascii=False)))
    try:
        note = sv.chat_json([{"role": "user", "content": prompt}])
        note["category"] = _clean_category(note.get("category"))
        proposed = note.pop("follow_up_question", None)
        state["note"] = note
    except Exception:
        # Structuring failed: keep the note we have, keep the conversation alive.
        state["note"].setdefault("verbatim_statements", []).append(english)
        proposed = None

    # Whether to ask is decided in code (deterministic, testable); what to ask comes from the model.
    missing = _missing_field(state["note"])
    follow_up = (proposed or GENERIC_QUESTIONS[missing]) if missing else None

    if follow_up and len(state["turns"]) < MAX_PATIENT_TURNS:
        reply = safety_filter(_hindi_reply(state, follow_up))
        save(state)
        return _reply(state, reply, done=False)

    booking = book(state["note"].get("category", "general"), urgent=False)
    state["booking"] = booking
    state["status"] = "booked"
    save(state)
    reply = safety_filter(
        f"आपकी बात नोट हो गई है। {booking['doctor']} से {booking['slot']} बजे appointment book हो गया है। जल्दी स्वस्थ होइए।"
    )
    return _reply(state, reply, done=True)


HINDI_FALLBACKS = {
    "What is troubling you the most right now?": "अभी आपको सबसे ज़्यादा क्या तकलीफ़ हो रही है?",
    "Since when has this been going on?": "यह तकलीफ़ कब से है?",
    "How bad is it — is it stopping you from doing your daily work?":
        "तकलीफ़ कितनी है — क्या इससे आपका रोज़ का काम रुक रहा है?",
}


def _translate_question(question: str) -> str:
    if question in HINDI_FALLBACKS:
        return HINDI_FALLBACKS[question]
    try:
        return sv.chat([{"role": "user", "content":
                         "Translate to natural spoken Hindi (Devanagari). Output only the "
                         f"translation:\n{question}"}]).strip().strip('"')
    except Exception:
        return "थोड़ा और बताइए।"


def _hindi_reply(state: dict, question: str) -> str:
    """Second, small call: confirm-back + follow-up in the patient's language."""
    note = state["note"]
    summary = ", ".join(filter(None, [
        note.get("chief_complaint"),
        f"duration {note['onset_duration']}" if note.get("onset_duration") else None,
    ]))
    if not summary:
        # Nothing captured yet: ask without a confirm-back rather than inventing one.
        return "ठीक है। " + _translate_question(question)
    corr = note.get("corrections") or []
    correction_line = (
        f"The patient corrected {corr[-1].get('field','a detail')} from "
        f"'{corr[-1].get('old')}' to '{corr[-1].get('new')}' — acknowledge the corrected value."
        if corr else "")
    prompt = (REPLY_PROMPT.replace("{SUMMARY}", summary)
              .replace("{CORRECTION}", correction_line)
              .replace("{QUESTION}", question))
    try:
        return sv.chat([{"role": "user", "content": prompt}]).strip().strip('"')
    except Exception:
        return "ठीक है, नोट कर लिया। थोड़ा और बताइए — तकलीफ़ कब से है और कैसी है?"


def _reply(state: dict, reply_text: str, done: bool) -> dict:
    audio = sv.tts(reply_text, language_code="hi-IN")
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    fname = f"reply_{state['id']}_{len(state['turns'])}.wav"
    (AUDIO_DIR / fname).write_bytes(audio)
    return {
        "session": state, "reply_text": reply_text,
        "reply_audio": f"/audio/{fname}", "done": done,
    }

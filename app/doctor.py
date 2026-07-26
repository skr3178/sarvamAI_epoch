"""Doctor-screen view model: the queue, its ticket numbers, and its translation table.

The clinician picks a reading language from a dropdown. Everything on the screen — the
fixed labels and the free text of each note — goes through one cache-first translation
pass, so switching language costs no request latency: the strings already cached come
back now, the rest arrive over the next couple of 2-second refreshes.

Translation here is for reading comfort only. The English original always stays on the
card (as a hover title), because the note is the clinical record and a machine
translation of it is not.
"""
import json

from . import agent, translate
from .languages import DEFAULT, SUPPORTED

# Fixed screen text, in English, translated through the same cache as the notes.
LABELS = {
    "title": "Intake queue",
    "tagline": "Notes assemble while the patient is still speaking · auto-refresh 2s",
    "language": "Reading language",
    "caveat": "Machine-translated for reading · hover any line for the English original",
    "translating": "translating",
    "intakes_today": "intakes today",
    "empty": "No intakes yet.",
    "ticket": "Ticket",
    "red_flag_badge": "RED FLAG — SEE NOW",
    "booked_badge": "BOOKED",
    "in_progress_badge": "INTAKE IN PROGRESS",
    "walk_in": "walk-in",
    "listening": "…listening",
    "red_flags": "Red flags",
    "complaint": "Complaint",
    "duration": "Duration",
    "severity": "Severity",
    "symptoms": "Symptoms",
    "medications": "Medications",
    "booked_with": "Booked with",
    "own_words": "Patient's own words (click to play)",
    "consider": "Areas to consider · clinician only",
}


def _sessions() -> list[dict]:
    """Every session with at least one turn, oldest first."""
    out = []
    for f in agent.DATA_DIR.glob("session_*.json"):
        try:
            s = json.loads(f.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if s.get("turns"):
            out.append(s)
    out.sort(key=lambda s: s.get("created", 0))
    return out


def _backfill_tickets(sessions: list[dict]) -> None:
    """Give a number to sessions recorded before ticketing existed, in arrival order."""
    for s in sessions:
        if not s.get("ticket"):
            s["ticket"] = agent.next_ticket()
            agent.save(s)


def _free_text(s: dict) -> list[str]:
    """Every clinician-readable string on a card that is worth translating."""
    note = s.get("note") or {}
    texts = [note.get("chief_complaint"), note.get("onset_duration"), note.get("severity_words")]
    for key in ("symptoms", "medications_mentioned", "areas_to_consider"):
        texts += note.get(key) or []
    for c in note.get("corrections") or []:
        texts += [c.get("old"), c.get("new")]
    texts += s.get("red_flags") or []
    texts += [t.get("english") for t in s.get("turns") or []]
    # Specialty is a role and translates well; the doctor's own name must not be touched.
    texts.append((s.get("booking") or {}).get("specialty"))
    return [t for t in texts if t]


def queue(lang: str) -> dict:
    """Doctor queue payload: escalations first, then most recent, plus its translations."""
    sessions = _sessions()
    _backfill_tickets(sessions)
    lang = lang if lang in SUPPORTED else DEFAULT

    wanted = list(LABELS.values()) + [t for s in sessions for t in _free_text(s)]
    tr, pending = translate.table(wanted, lang)

    sessions.sort(key=lambda s: (s.get("status") != "escalated", -s.get("created", 0)))
    return {
        "lang": lang,
        "labels": {k: tr.get(v, v) for k, v in LABELS.items()},
        "sessions": sessions,
        "tr": tr,
        "pending": pending,
    }

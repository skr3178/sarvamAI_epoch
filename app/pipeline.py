"""M1 ugly end-to-end pipeline: one audio clip -> intake note + booking/escalation + spoken reply.

Usage: python -m app.pipeline app/audio/test_patient.wav
"""
import json
import re
import sys
from pathlib import Path

from . import redflags, sarvam_client as sv

DOCTOR_ROSTER = [
    {"name": "Dr. Meera Nair", "specialty": "General Medicine", "categories": ["fever", "stomach", "general", "weakness", "infection"], "slots": ["12:40", "1:00", "1:20"]},
    {"name": "Dr. Arjun Rao", "specialty": "Orthopedics", "categories": ["joint", "bone", "back", "injury"], "slots": ["12:50", "1:30"]},
    {"name": "Dr. Sania Khan", "specialty": "ENT", "categories": ["ear", "throat", "nose", "cough"], "slots": ["1:10", "1:50"]},
    {"name": "URGENT — Duty Doctor", "specialty": "Emergency", "categories": ["urgent"], "slots": ["NOW"]},
]

EXTRACT_PROMPT = """You are a medical intake structuring engine for an Indian clinic. You NEVER diagnose.
From the patient's translated statement below, return ONLY a JSON object:
{
  "chief_complaint": "...",
  "symptoms": ["..."],
  "onset_duration": "... (honor any self-correction: the LAST stated value wins)",
  "corrections": [{"field": "...", "old": "...", "new": "..."}],
  "severity_words": "patient's own words about severity, or null",
  "medications_mentioned": [],
  "age": null,
  "confidence": {"chief_complaint": 0.0-1.0, "onset_duration": 0.0-1.0, "age": 0.0-1.0},
  "category": "one of: fever|stomach|general|weakness|infection|joint|bone|back|injury|ear|throat|nose|cough",
  "areas_to_consider": ["clinician-only: symptom areas worth exploring, NEVER a diagnosis"],
  "follow_up_question": "the single most useful next question, plain language, non-leading"
}

Patient said (English translation): {STATEMENT}"""

# Patient-facing text must never contain diagnosis/advice language (safety boundary, in code).
FORBIDDEN_PATIENT_FACING = re.compile(
    r"you (probably|likely|may) have|diagnos|it is (just|only)|don'?t worry|nothing serious|"
    r"take (this|these|paracetamol|antibiotic)|you should take|prescri", re.IGNORECASE)


def safety_filter(text: str) -> str:
    if FORBIDDEN_PATIENT_FACING.search(text):
        return "Aapki baat note kar li gayi hai. Doctor aapse jald milenge."
    return text


def book(category: str, urgent: bool) -> dict:
    if urgent:
        doc = DOCTOR_ROSTER[-1]
    else:
        doc = next((d for d in DOCTOR_ROSTER if category in d["categories"]), DOCTOR_ROSTER[0])
    return {"doctor": doc["name"], "specialty": doc["specialty"], "slot": doc["slots"][0]}


def run(audio_path: str) -> dict:
    stt = sv.stt_translate(audio_path)
    english = stt["transcript"]
    lang = stt.get("language_code") or "hi-IN"

    flags = redflags.check(english)
    if flags:
        booking = book("urgent", urgent=True)
        note = {
            "urgency": "RED — same-turn escalation",
            "red_flags": flags,
            "verbatim_translation": english,
            "booking": booking,
        }
        reply = "Yeh zaroori hai — main abhi staff ko bula rahi hoon. Kripya wahin rahiye."
    else:
        extracted = sv.chat_json([
            {"role": "user", "content": EXTRACT_PROMPT.replace("{STATEMENT}", english)}
        ])
        booking = book(extracted.get("category", "general"), urgent=False)
        note = {
            "urgency": "ROUTINE",
            "verbatim_translation": english,
            **extracted,
            "booking": booking,
        }
        reply = safety_filter(
            f"Aapki baat note ho gayi hai. {booking['doctor']} se {booking['slot']} baje appointment book ho gaya hai."
        )

    reply_audio = sv.tts(reply, language_code="hi-IN")
    out_dir = Path(audio_path).parent
    (out_dir / "reply.wav").write_bytes(reply_audio)
    note["patient_language"] = lang
    note["spoken_reply"] = reply
    return note


if __name__ == "__main__":
    result = run(sys.argv[1])
    print(json.dumps(result, indent=2, ensure_ascii=False))

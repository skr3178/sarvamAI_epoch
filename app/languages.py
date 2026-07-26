"""Language support for the patient kiosk.

Every fixed string the patient hears or reads is authored in English here and translated
once per language into a disk cache. Nothing in the conversational path calls the translate
API, so adding languages costs no turn latency.

The language list is not the vendor's documented list — it is what this account can actually
speak, verified by probing the TTS endpoint. Saaras accepts far more languages as input than
Bulbul can produce as output, and the kiosk may only offer languages the agent can reply in.

Rebuild the cache after editing STRINGS:  python3 -m app.languages
"""
import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import sarvam_client as sv

CACHE_DIR = Path(__file__).resolve().parent / "data" / "strings"

# (code, English name, endonym). Verified against text-to-speech on 2026-07-26; the remaining
# bulbul:v3 languages return "request beta access" on this account and are deliberately absent.
LANGUAGES = [
    ("hi-IN", "Hindi", "हिन्दी"),
    ("bn-IN", "Bengali", "বাংলা"),
    ("mr-IN", "Marathi", "मराठी"),
    ("te-IN", "Telugu", "తెలుగు"),
    ("ta-IN", "Tamil", "தமிழ்"),
    ("gu-IN", "Gujarati", "ગુજરાતી"),
    ("kn-IN", "Kannada", "ಕನ್ನಡ"),
    ("ml-IN", "Malayalam", "മലയാളം"),
    ("pa-IN", "Punjabi", "ਪੰਜਾਬੀ"),
    ("od-IN", "Odia", "ଓଡ଼ିଆ"),
    ("en-IN", "English", "English"),
]

SUPPORTED = {code for code, _, _ in LANGUAGES}
DEFAULT = "hi-IN"

# A voice per language. bulbul:v2 exposes one shared set of speakers across languages;
# anushka is the warm register chosen for healthcare.
SPEAKER = "anushka"

# Source strings. Keys prefixed q_ are spoken questions; ui_ are screen text.
STRINGS = {
    "q_chief_complaint": "What is troubling you the most right now?",
    "q_onset_duration": "Since when has this been going on?",
    "q_severity_words": "How bad is it? Is it stopping you from doing your daily work?",
    "q_associated": "Is anything else happening along with it, like fever, vomiting, or pain somewhere else?",
    "ack": "Alright.",
    "escalation": "This is urgent. I am calling the staff right now. Please stay where you are.",
    "garbled": "Sorry, I could not hear that clearly. Please tell me again.",
    "booked": "I have noted everything. Your appointment is booked with {doctor} at {slot}. Get well soon.",
    "safety_fallback": "I have noted what you said. The doctor will see you shortly.",
    "ui_title": "Tell us your problem in your own language",
    "ui_press_speak": "Press to speak",
    "ui_press_stop": "Press to stop",
    "ui_hint": "Press the button and speak. Press again when you are finished.",
    "ui_listening": "Listening...",
    "ui_thinking": "Understanding...",
    "ui_your_turn": "Press the button to answer",
    "ui_booked": "Appointment booked",
    "ui_escalated": "Staff have been alerted",
    "ui_error": "Something went wrong. Please try again.",
    "ui_mic_blocked": "Microphone unavailable. Open this page over localhost or HTTPS.",
    "ui_language": "Language",
}


def _cache_file(lang: str) -> Path:
    return CACHE_DIR / f"{lang}.json"


def _translate(text: str, target: str) -> str:
    return sv.translate(text, target, source="en-IN")


def build(lang: str) -> dict:
    """Translate every string into `lang` and cache it. English is the source, so it is identity."""
    if lang == "en-IN":
        strings = dict(STRINGS)
    else:
        with ThreadPoolExecutor(max_workers=3) as pool:
            keys = list(STRINGS)
            translated = pool.map(lambda k: _translate(STRINGS[k], lang), keys)
            strings = dict(zip(keys, translated))
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    _cache_file(lang).write_text(json.dumps(strings, ensure_ascii=False, indent=1))
    return strings


_memo: dict[str, dict] = {}


def strings(lang: str) -> dict:
    """Localized strings for `lang`, falling back to English for anything missing.

    Never raises and never blocks on the network in the request path: an uncached language
    yields English rather than a 20s translate round-trip mid-conversation.
    """
    lang = lang if lang in SUPPORTED else DEFAULT
    if lang not in _memo:
        try:
            _memo[lang] = json.loads(_cache_file(lang).read_text())
        except (OSError, json.JSONDecodeError):
            _memo[lang] = dict(STRINGS)
    return {**STRINGS, **_memo[lang]}


def t(lang: str, key: str, **fmt) -> str:
    text = strings(lang).get(key, STRINGS.get(key, ""))
    if fmt:
        try:
            return text.format(**fmt)
        except (KeyError, IndexError, ValueError):
            # A translation mangled a placeholder; fall back to the English frame.
            return STRINGS[key].format(**fmt)
    return text


if __name__ == "__main__":
    for code, name, _ in LANGUAGES:
        try:
            built = build(code)
            print(f"{code} {name:<10} cached {len(built)} strings")
        except Exception as e:
            print(f"{code} {name:<10} FAILED: {type(e).__name__}: {e}")

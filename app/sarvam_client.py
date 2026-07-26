"""Thin wrappers around the three Sarvam APIs used by the intake agent."""
import base64
import json
import os
import re
from pathlib import Path

import requests

BASE = "https://api.sarvam.ai"
_KEY = None


def api_key() -> str:
    global _KEY
    if _KEY is None:
        keyfile = Path(__file__).resolve().parent.parent / "api_key.md"
        _KEY = os.environ.get("SARVAM_API_KEY") or keyfile.read_text().strip()
    return _KEY


def _mime(path: str) -> str:
    return {"wav": "audio/wav", "webm": "audio/webm", "mp3": "audio/mpeg", "ogg": "audio/ogg",
            "mp4": "audio/mp4", "m4a": "audio/mp4", "aac": "audio/aac"}.get(
        Path(path).suffix.lstrip(".").lower(), "audio/wav")


def stt_translate(audio_path: str) -> dict:
    """Code-mixed Indic speech -> English translation. Returns {transcript, language_code}."""
    with open(audio_path, "rb") as f:
        r = requests.post(
            f"{BASE}/speech-to-text-translate",
            headers={"api-subscription-key": api_key()},
            files={"file": (Path(audio_path).name, f, _mime(audio_path))},
            data={"model": "saaras:v2.5"},
            timeout=120,
        )
    r.raise_for_status()
    return r.json()


def stt_verbatim(audio_path: str) -> dict:
    """Native-script transcript of the same audio (for verbatim quotes)."""
    with open(audio_path, "rb") as f:
        r = requests.post(
            f"{BASE}/speech-to-text",
            headers={"api-subscription-key": api_key()},
            files={"file": (Path(audio_path).name, f, _mime(audio_path))},
            data={"model": "saarika:v2.5"},
            timeout=120,
        )
    r.raise_for_status()
    return r.json()


def tts(text: str, language_code: str = "hi-IN", speaker: str = "anushka") -> bytes:
    """Text -> wav bytes via Bulbul."""
    r = requests.post(
        f"{BASE}/text-to-speech",
        headers={"api-subscription-key": api_key(), "Content-Type": "application/json"},
        json={
            "text": text,
            "target_language_code": language_code,
            "speaker": speaker,
            "model": "bulbul:v2",
        },
        timeout=120,
    )
    r.raise_for_status()
    return base64.b64decode(r.json()["audios"][0])


# Starter tier caps total tokens (reasoning + content) at 4096 per call, so prompts are
# kept small and the turn is split into two focused calls rather than one large one.
MAX_TOKENS = 4096


def chat(messages: list, model: str = "sarvam-30b", max_tokens: int = MAX_TOKENS) -> str:
    r = requests.post(
        f"{BASE}/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key()}", "Content-Type": "application/json"},
        json={
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "reasoning_effort": "low",
        },
        timeout=180,
    )
    r.raise_for_status()
    content = r.json()["choices"][0]["message"]["content"]
    if content is None:
        raise RuntimeError("model returned no content (reasoning budget exhausted)")
    return content


def chat_json(messages: list, model: str = "sarvam-105b", **kw) -> dict:
    """Chat call whose reply must parse as a JSON object; strips code fences.

    Defaults to 105b: on structuring prompts 30b spends the whole 4096-token budget
    reasoning and returns no content. Falls back to 30b with a '{' prefill, which
    shortens its reasoning enough to finish.
    """
    try:
        text = chat(messages, model=model, **kw)
    except (RuntimeError, requests.HTTPError):
        text = "{" + chat(messages + [{"role": "assistant", "content": "{"}],
                          model="sarvam-30b", **kw)
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        raise ValueError(f"no JSON object in model reply: {text[:200]}")
    return json.loads(m.group(0))

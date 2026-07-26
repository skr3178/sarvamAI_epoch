"""Thin wrappers around the three Sarvam APIs used by the intake agent."""
import base64
import json
import os
import random
import re
import time
from pathlib import Path

import requests

BASE = "https://api.sarvam.ai"
_KEY = None

RETRY_STATUS = {429, 500, 502, 503, 504}
MAX_ATTEMPTS = 4


def _post(url: str, *, attempts: int = MAX_ATTEMPTS, **kw) -> requests.Response:
    """POST with backoff on rate limits and transient upstream errors.

    The starter tier rate-limits readily under any concurrency, and a 429 during a live
    intake would drop the patient's turn, so retrying is the difference between a pause
    and a failed conversation.
    """
    delay = 1.0
    for attempt in range(1, attempts + 1):
        try:
            r = requests.post(url, **kw)
        except (requests.ConnectionError, requests.Timeout):
            if attempt == attempts:
                raise
        else:
            if r.status_code not in RETRY_STATUS or attempt == attempts:
                r.raise_for_status()
                return r
            # Honour Retry-After when the server sends one.
            try:
                delay = max(delay, float(r.headers.get("Retry-After", 0)))
            except ValueError:
                pass
        time.sleep(delay + random.uniform(0, 0.4))
        delay = min(delay * 2, 16.0)
    raise RuntimeError(f"exhausted {attempts} attempts: {url}")


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
        r = _post(
            f"{BASE}/speech-to-text-translate",
            headers={"api-subscription-key": api_key()},
            files={"file": (Path(audio_path).name, f, _mime(audio_path))},
            data={"model": "saaras:v2.5"},
            timeout=120,
        )
    return r.json()


def stt_verbatim(audio_path: str) -> dict:
    """Native-script transcript of the same audio (for verbatim quotes)."""
    with open(audio_path, "rb") as f:
        r = _post(
            f"{BASE}/speech-to-text",
            headers={"api-subscription-key": api_key()},
            files={"file": (Path(audio_path).name, f, _mime(audio_path))},
            data={"model": "saarika:v2.5"},
            timeout=120,
        )
    return r.json()


def translate(text: str, target: str, source: str = "en-IN") -> str:
    """Text -> target language via Mayura (11 Indic languages, context-preserving)."""
    r = _post(
        f"{BASE}/translate",
        headers={"api-subscription-key": api_key(), "Content-Type": "application/json"},
        json={"input": text[:900], "source_language_code": source,
              "target_language_code": target, "model": "mayura:v1"},
        timeout=60,
    )
    return r.json()["translated_text"]


def tts(text: str, language_code: str = "hi-IN", speaker: str = "anushka") -> bytes:
    """Text -> wav bytes via Bulbul."""
    r = _post(
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
    return base64.b64decode(r.json()["audios"][0])


# Starter tier caps total tokens (reasoning + content) at 4096 per call, so prompts are
# kept small and the turn is split into two focused calls rather than one large one.
MAX_TOKENS = 4096


def chat(messages: list, model: str = "sarvam-30b", max_tokens: int = MAX_TOKENS) -> str:
    r = _post(
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

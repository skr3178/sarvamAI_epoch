"""On-demand translation of free text, cached to disk, never blocking a request.

The intake note is authored in English (Saaras translates every patient utterance on the
way in), but the clinician reading it may not be an English reader. This module lets any
screen ask for a language without paying translation latency in the request path:
`table()` returns whatever is already cached and hands the misses to a background pool,
so the caller's poll loop picks them up a second or two later.

Every string is cached forever under data/translations/<lang>.json, keyed by its English
source. Clinic text repeats heavily — the same labels, doctor names, specialties and red
flags across every card — so the cache saturates within the first few intakes and a
language costs its translations once for the whole clinic, not once per refresh.
"""
import json
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import sarvam_client as sv
from .languages import SUPPORTED

CACHE_DIR = Path(__file__).resolve().parent / "data" / "translations"
SOURCE = "en-IN"

# Cap how many fresh strings one request may queue. A doctor switching language with a
# full queue on screen would otherwise fire a hundred calls at a rate-limited tier at once;
# instead the queue fills in over the next few 2-second refreshes.
MAX_NEW_PER_REQUEST = 32

_pool = ThreadPoolExecutor(max_workers=4)
_lock = threading.Lock()
_cache: dict[str, dict[str, str]] = {}          # lang -> {english: translated}
_inflight: set[tuple[str, str]] = set()         # (lang, english) currently being fetched


def _cache_file(lang: str) -> Path:
    return CACHE_DIR / f"{lang}.json"


def _table(lang: str) -> dict:
    """Cached table for `lang`, loaded from disk on first use. Call under _lock."""
    if lang not in _cache:
        try:
            _cache[lang] = json.loads(_cache_file(lang).read_text())
        except (OSError, json.JSONDecodeError):
            _cache[lang] = {}
    return _cache[lang]


def _store(lang: str, text: str, translated: str) -> None:
    with _lock:
        table = _table(lang)
        table[text] = translated
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        _cache_file(lang).write_text(json.dumps(table, ensure_ascii=False, indent=1))


def _fetch(lang: str, text: str) -> None:
    try:
        _store(lang, text, sv.translate(text, lang, source=SOURCE))
    except Exception:
        pass  # leave it uncached; a later refresh retries it
    finally:
        with _lock:
            _inflight.discard((lang, text))


def translatable(text) -> bool:
    """Worth an API call? Skip blanks and bare numbers/codes ('T-004', '1:20', '38')."""
    text = str(text or "").strip()
    return bool(text) and any(c.isalpha() for c in text) and len(text) > 1


def table(texts, lang: str) -> tuple[dict[str, str], int]:
    """({english: translated} for what is cached, count still being fetched).

    Missing keys are the caller's cue to render the English — the translation lands in
    the cache shortly and the next call returns it.
    """
    if lang == SOURCE or lang not in SUPPORTED:
        return {}, 0
    wanted = [t for t in dict.fromkeys(str(x) for x in texts) if translatable(t)]
    with _lock:
        cached = _table(lang)
        out = {t: cached[t] for t in wanted if t in cached}
        missing = [t for t in wanted if t not in cached]
        fresh = [t for t in missing if (lang, t) not in _inflight][:MAX_NEW_PER_REQUEST]
        _inflight.update((lang, t) for t in fresh)
    for t in fresh:
        _pool.submit(_fetch, lang, t)
    return out, len(missing)

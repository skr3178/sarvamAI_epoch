"""Shared eval harness: patient-audio cache, channel degradation, conversation driver.

Every suite in eval/ goes through here. Three pieces:

  speak()            Bulbul TTS of one patient utterance, cached on disk by content hash.
                     The cache is the whole economy of this eval: the Sarvam tier is
                     rate-limited, so a fixture is synthesized once and reused by every
                     suite and every rerun. Nothing here calls the API if the file exists.
  degrade()          clean / phone / noisy channel simulation via ffmpeg, cached the same way.
  run_conversation() drives the REAL agent (app.agent.process_turn) over a scripted patient.

Smoke test: cd /home/skr/Downloads/sarvam && python3 -m eval.harness
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

from app import agent, sarvam_client as sv

FIXTURES = Path(__file__).resolve().parent / "fixtures"
AUDIO_DIR = FIXTURES / "audio"          # speak() output, one wav per (text, lang, speaker)
DEGRADED_DIR = FIXTURES / "degraded"    # degrade() output, one wav per (source, condition)

CONDITIONS = ("clean", "phone", "noisy")
FFMPEG = shutil.which("ffmpeg") or "/usr/bin/ffmpeg"
FFPROBE = shutil.which("ffprobe") or "/usr/bin/ffprobe"

SNR_DB = 10.0            # target signal-to-noise for the "noisy" condition
NOISE_AMPLITUDE = 0.5    # anoisesrc amplitude; actual level is measured, not assumed
MIX_HEADROOM_DB = 1.5    # applied to signal+noise together, so it does not change SNR
SETTLE_WAIT_S = 45       # wait for the agent's background note structuring before scoring


# ---------------------------------------------------------------- small utilities

def _digest(*parts: str) -> str:
    h = hashlib.sha1("\x1f".join(parts).encode("utf-8")).hexdigest()
    return h[:16]


def _file_digest(path: Path) -> str:
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def _publish(tmp: Path, dest: Path) -> Path:
    """Rename into place. Cache hits are existence checks, and other agents run
    concurrently, so a half-written wav must never be visible under its final name."""
    os.replace(tmp, dest)
    return dest


def _write_atomic(dest: Path, data: bytes) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=dest.parent, suffix=".part")
    with os.fdopen(fd, "wb") as f:
        f.write(data)
    return _publish(Path(tmp), dest)


def _cached(path: Path) -> bool:
    return path.exists() and path.stat().st_size > 0


def _ffmpeg(args: list[str]) -> subprocess.CompletedProcess:
    proc = subprocess.run([FFMPEG, "-hide_banner", "-nostdin", "-y", *args],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"ffmpeg failed: {' '.join(args)}\n{proc.stderr[-800:]}")
    return proc


def _sample_rate(wav: Path) -> int:
    proc = subprocess.run(
        [FFPROBE, "-v", "error", "-select_streams", "a:0",
         "-show_entries", "stream=sample_rate", "-of", "csv=p=0", str(wav)],
        capture_output=True, text=True)
    try:
        return int(proc.stdout.strip())
    except ValueError:
        return 22050  # Bulbul's native rate


_MEAN_DB = re.compile(r"mean_volume:\s*(-?[\d.]+|-inf) dB")


def _mean_dbfs(input_args: list[str]) -> float:
    """RMS level of an ffmpeg input, in dBFS, via volumedetect."""
    proc = _ffmpeg([*input_args, "-af", "volumedetect", "-f", "null", "-"])
    m = _MEAN_DB.search(proc.stderr)
    if not m or m.group(1) == "-inf":
        return -90.0
    return float(m.group(1))


_NOISE_DBFS: dict[int, float] = {}


def _noise_dbfs(rate: int) -> float:
    """Measured RMS of the noise source, so the mix gain is derived rather than guessed."""
    if rate not in _NOISE_DBFS:
        _NOISE_DBFS[rate] = _mean_dbfs([
            "-f", "lavfi", "-i",
            f"anoisesrc=color=white:sample_rate={rate}:amplitude={NOISE_AMPLITUDE}:duration=3"])
    return _NOISE_DBFS[rate]


# ---------------------------------------------------------------- 1. patient audio

def speak(text: str, language_code: str = "hi-IN", speaker: str = "anushka") -> Path:
    """Synthesize one patient utterance. Returns the cached wav if it already exists."""
    path = AUDIO_DIR / f"{language_code}_{speaker}_{_digest(text, language_code, speaker)}.wav"
    if _cached(path):
        return path
    audio = sv.tts(text, language_code=language_code, speaker=speaker)
    _write_atomic(path, audio)
    # Sidecar, not a shared manifest: concurrent suites must never contend on one file.
    _write_atomic(path.with_suffix(".json"), json.dumps(
        {"text": text, "language_code": language_code, "speaker": speaker},
        ensure_ascii=False, indent=1).encode("utf-8"))
    return path


# ---------------------------------------------------------------- 2. channel degradation

def _phone(src: Path, dest: Path) -> None:
    """8 kHz telephony band + a real GSM 06.10 codec round-trip, then back to 16 kHz wav
    (Saaras takes wav; the point is the codec damage, not the container)."""
    with tempfile.TemporaryDirectory() as td:
        narrowband = Path(td) / "narrowband.gsm"
        _ffmpeg(["-i", str(src), "-ac", "1", "-ar", "8000",
                 "-af", "highpass=f=300,lowpass=f=3400",
                 "-c:a", "libgsm", "-f", "gsm", str(narrowband)])
        _ffmpeg(["-i", str(narrowband), "-ac", "1", "-ar", "16000",
                 "-c:a", "pcm_s16le", str(dest)])


def _noisy(src: Path, dest: Path) -> None:
    """Additive white noise at ~SNR_DB. Levels are measured on both sides so the SNR is
    real; amix normalize=0 keeps it a plain sum, and the headroom trim avoids clipping."""
    rate = _sample_rate(src)
    gain_db = _mean_dbfs(["-i", str(src)]) - SNR_DB - _noise_dbfs(rate)
    _ffmpeg([
        "-i", str(src),
        "-filter_complex",
        f"anoisesrc=color=white:sample_rate={rate}:amplitude={NOISE_AMPLITUDE},"
        f"volume={gain_db:.2f}dB[n];"
        f"[0:a][n]amix=inputs=2:duration=first:normalize=0,volume=-{MIX_HEADROOM_DB}dB[m]",
        "-map", "[m]", "-ac", "1", "-ar", str(rate), "-c:a", "pcm_s16le", str(dest)])


def degrade(wav: Path, condition: str = "clean") -> Path:
    """Apply a channel condition to a wav. Never mutates the source; cached per (source, condition)."""
    wav = Path(wav)
    if condition not in CONDITIONS:
        raise ValueError(f"unknown condition {condition!r}, expected one of {CONDITIONS}")
    if condition == "clean":
        return wav
    dest = DEGRADED_DIR / f"{_file_digest(wav)}_{condition}.wav"
    if _cached(dest):
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=dest.parent, suffix=".part.wav")
    os.close(fd)
    tmp = Path(tmp)
    try:
        (_phone if condition == "phone" else _noisy)(wav, tmp)
        return _publish(tmp, dest)
    finally:
        tmp.unlink(missing_ok=True)


# ---------------------------------------------------------------- 3. conversation driver

def _settle(state: dict, timeout: float = SETTLE_WAIT_S) -> dict:
    """The agent structures the note on a background thread and answers the patient without
    waiting for it. Scoring does need it, so block here — after the clock has stopped."""
    sid = state.get("id")
    if not sid:
        return state
    job = getattr(agent, "_jobs", {}).get(sid)
    if job is not None:
        try:
            job.result(timeout=timeout)
        except Exception:
            pass
    try:
        return agent.load(sid)
    except Exception:
        return state


def run_conversation(utterances: list[str], condition: str = "clean", phone: str | None = None,
                     language_code: str = "hi-IN", speaker: str = "anushka") -> dict:
    """Drive a full multi-turn interview against the real agent.

    Stops as soon as a reply payload is done=True (booked or escalated), or on the first
    error — a broken turn is recorded, not raised, so one bad run cannot kill a matrix.
    turn_seconds measures process_turn only: TTS of the patient's line is the test rig,
    not agent latency.
    """
    state = agent.new_session(phone)
    replies: list[dict] = []
    turn_seconds: list[float] = []
    error = None
    spoken = 0

    for text in utterances:
        try:
            wav = degrade(speak(text, language_code, speaker), condition)
            started = time.monotonic()
            reply = agent.process_turn(state, str(wav))
            turn_seconds.append(time.monotonic() - started)
        except Exception as e:
            error = f"turn {spoken + 1}: {type(e).__name__}: {e}"
            break
        spoken += 1
        replies.append(reply)
        state = reply.get("session") or state
        if reply.get("done"):
            break

    return {
        "session": _settle(state),
        "replies": replies,
        "turn_seconds": turn_seconds,
        "condition": condition,
        "utterances": list(utterances),
        "stopped_early": spoken < len(utterances),
        "error": error,
    }


if __name__ == "__main__":
    result = run_conversation(
        ["मुझे दो दिन से बुखार है।", "सिर में भी दर्द है।"],
        condition="clean", phone="9999900000")
    session = result["session"]
    print(json.dumps({
        "condition": result["condition"],
        "stopped_early": result["stopped_early"],
        "error": result["error"],
        "turn_seconds": [round(s, 2) for s in result["turn_seconds"]],
        "transcripts": [t["english"] for t in session["turns"]],
        "replies": [r["reply_text"] for r in result["replies"]],
        "status": session["status"],
        "booking": session["booking"],
        "red_flags": session["red_flags"],
        "note": session["note"],
    }, ensure_ascii=False, indent=2))

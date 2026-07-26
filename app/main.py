"""FastAPI server: patient kiosk + doctor screen + turn API.

Run: uvicorn app.main:app --host 0.0.0.0 --port 8000
"""
from pathlib import Path

from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from . import agent, doctor, languages as L

app = FastAPI(title="Clinic Voice Intake")
STATIC = Path(__file__).resolve().parent / "static"


@app.get("/api/languages")
def languages():
    """Languages the agent can actually speak, with their localized UI strings."""
    return {
        "default": L.DEFAULT,
        "languages": [{"code": c, "name": n, "native": e} for c, n, e in L.LANGUAGES],
        "strings": {c: L.strings(c) for c, _, _ in L.LANGUAGES},
    }


@app.post("/api/session/new")
def session_new(phone: str = Form(default=""), language: str = Form(default=L.DEFAULT)):
    return agent.new_session(phone=phone or None, language=language)


@app.post("/api/turn/{sid}")
async def turn(sid: str, audio: UploadFile):
    state = agent.load(sid)
    agent.AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    ctype = (audio.content_type or "") + " " + (audio.filename or "")
    suffix = next((e for e in ("webm", "mp4", "ogg", "mp3") if e in ctype), "wav")
    fname = f"patient_{sid}_{len(state['turns']) + 1}.{suffix}"
    dest = agent.AUDIO_DIR / fname
    dest.write_bytes(await audio.read())
    try:
        return agent.process_turn(state, str(dest))
    except Exception as e:  # keep the kiosk alive; ask the patient to retry
        return JSONResponse({"session": state, "done": False, "error": str(e),
                             "reply_text": "माफ़ कीजिए, एक तकनीकी दिक्कत हुई। कृपया फिर से बताइए।",
                             "reply_audio": None}, status_code=200)


@app.get("/api/session/{sid}")
def session_get(sid: str):
    return agent.load(sid)


@app.get("/api/sessions")
def sessions_all(lang: str = "en-IN"):
    """Doctor queue, read in `lang`. The notes themselves stay English on disk."""
    return doctor.queue(lang)


@app.get("/audio/{fname}")
def audio_file(fname: str):
    return FileResponse(agent.AUDIO_DIR / Path(fname).name)


@app.get("/")
def landing_page():
    """Fork in the corridor: patients one way, staff the other."""
    return FileResponse(STATIC / "landing.html")


@app.get("/patient")
def patient_page():
    return FileResponse(STATIC / "patient.html")


@app.get("/doctor")
def doctor_page():
    return FileResponse(STATIC / "doctor.html")


app.mount("/static", StaticFiles(directory=STATIC), name="static")

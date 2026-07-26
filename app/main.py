"""FastAPI server: patient kiosk + doctor screen + turn API.

Run: uvicorn app.main:app --host 0.0.0.0 --port 8000
"""
from pathlib import Path

from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from . import agent

app = FastAPI(title="Clinic Voice Intake")
STATIC = Path(__file__).resolve().parent / "static"


@app.post("/api/session/new")
def session_new(phone: str = Form(default="")):
    state = agent.new_session(phone=phone or None)
    return state


@app.post("/api/turn/{sid}")
async def turn(sid: str, audio: UploadFile):
    state = agent.load(sid)
    agent.AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    suffix = "webm" if "webm" in (audio.content_type or "") else "wav"
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


@app.get("/audio/{fname}")
def audio_file(fname: str):
    return FileResponse(agent.AUDIO_DIR / Path(fname).name)


@app.get("/")
def patient_page():
    return FileResponse(STATIC / "patient.html")


@app.get("/doctor")
def doctor_page():
    return FileResponse(STATIC / "doctor.html")


app.mount("/static", StaticFiles(directory=STATIC), name="static")

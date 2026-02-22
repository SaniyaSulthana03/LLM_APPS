from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import shutil
import os
import uvicorn

from mic import transcribe_audio
from tts import text_to_speech
from ocr import extract_text_from_image
from text_summarization import summarize_text_with_rag

app = FastAPI(title="Multimodal AI API", version="1.0")

os.makedirs("outputs", exist_ok=True)


@app.get("/")
def home():
    return {"message": "Multimodal AI API running"}


@app.post("/stt")
async def speech_to_text(file: UploadFile = File(...)):
    path = f"outputs/{file.filename}"

    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    transcription = transcribe_audio(path)

    return {"transcription": transcription}


@app.post("/tts")
async def tts_api(text: str = Form(...)):
    audio_path = text_to_speech(text)
    return {"audio_file": audio_path}


@app.post("/ocr")
async def image_ocr(file: UploadFile = File(...)):
    path = f"outputs/{file.filename}"

    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    summary = extract_text_from_image(path)
    return {"summary": summary}


@app.post("/rag")
async def rag(file: UploadFile = File(...)):
    path = f"outputs/{file.filename}"

    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    summary = summarize_text_with_rag(path)
    return {"summary": summary}


@app.get("/audio/{filename}")
def get_audio(filename: str):
    path = f"outputs/{filename}"
    return FileResponse(path, media_type="audio/wav")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
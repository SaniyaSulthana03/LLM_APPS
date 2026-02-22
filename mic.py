from faster_whisper import WhisperModel
from datetime import datetime
import os

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8"
)

HISTORY_FILE = "voice_history.txt"


def transcribe_audio(file_path: str) -> str:
    if not os.path.exists(file_path):
        raise FileNotFoundError("Audio file not found")

    segments, _ = model.transcribe(
        file_path,
        language="en"
    )

    text = " ".join(seg.text for seg in segments).strip()

    save_history(text)

    return text


def save_history(text: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}\n{text}\n{'-'*40}\n")
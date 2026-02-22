from gtts import gTTS
from datetime import datetime
import os

TTS_HISTORY_FILE = "tts_history.txt"
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_tts_history(text, audio_file):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(TTS_HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"Time: {timestamp}\n")
        f.write(f"Text Input (English): {text}\n")
        f.write(f"Audio File: {audio_file}\n")
        f.write("-" * 50 + "\n")

def text_to_speech(text: str) -> str:
    """
    Converts text to speech and saves as MP3.
    Returns audio file path.
    """

    filename = f"tts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    audio_path = os.path.join(OUTPUT_DIR, filename)

    tts = gTTS(text=text, lang="en")
    tts.save(audio_path)

    save_tts_history(text, audio_path)

    return audio_path
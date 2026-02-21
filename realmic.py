import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
from faster_whisper import WhisperModel
from datetime import datetime

SAMPLE_RATE = 16000  #Hz
DURATION = 5  
OUTPUT_FILE = "live_audio.wav"


model = WhisperModel(
    "small",
    device="cpu",      
    compute_type="int8"
)

def record_audio():
    print(" Recording... Speak now")
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype=np.int16
    )
    sd.wait()
    wav.write(OUTPUT_FILE, SAMPLE_RATE, audio)
    print("Recording complete")

def transcribe_audio():
    # small pieces of recognized speech
    # info : metadata
    segments, info = model.transcribe(
        OUTPUT_FILE,
        language="en",       
        task="transcribe"    
    )

    spoken_text = "".join([seg.text for seg in segments])
    final_text = spoken_text  # same for now

    print("\n Spoken (English):")
    print(spoken_text)

    print("\n Transcribed (English):")
    print(final_text)

    save_history(spoken_text, final_text)

HISTORY_FILE = "voice_history.txt"

def save_history(spoken_text, final_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"Time: {timestamp}\n")
        f.write(f"Spoken (English): {spoken_text}\n")
        f.write(f"Transcribed (English): {final_text}\n")
        f.write("-" * 50 + "\n")


if __name__ == "__main__":
    input("Press ENTER to start recording...")
    record_audio()
    transcribe_audio()
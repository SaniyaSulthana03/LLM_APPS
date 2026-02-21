# TTS_HISTORY_FILE = "tts_history.txt"

# from datetime import datetime
# import pyttsx3

# def save_tts_history(text):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     with open(TTS_HISTORY_FILE, "a", encoding="utf-8") as f:
#         f.write(f"Time: {timestamp}\n")
#         f.write(f"Text Input (English): {text}\n")
#         f.write("-" * 50 + "\n")


# # Initialize TTS engine
# tts_engine = pyttsx3.init()

# # Force English voice
# voices = tts_engine.getProperty("voices")
# for voice in voices:
#     if "english" in voice.name.lower():
#         tts_engine.setProperty("voice", voice.id)
#         break

# tts_engine.setProperty("rate", 160)   # speaking speed
# tts_engine.setProperty("volume", 1.0) # volume (0–1)

# def text_to_speech(text):
#     print("\n🔊 Speaking:")
#     print(text)

#     # Speak
#     tts_engine.say(text)
#     tts_engine.runAndWait()

#     # Save history
#     save_tts_history(text)   




# # def text_to_speech(text):
# #     print("\n🔊 Speaking:")
# #     print(text)

# #     # ✅ Re-initialize engine EVERY time
# #     engine = pyttsx3.init()

# #     # Force English voice
# #     voices = engine.getProperty("voices")
# #     for voice in voices:
# #         if "english" in voice.name.lower():
# #             engine.setProperty("voice", voice.id)
# #             break

# #     engine.setProperty("rate", 160)
# #     engine.setProperty("volume", 1.0)

# #     engine.say(text)
# #     engine.runAndWait()

# #     engine.stop()  # VERY IMPORTANT

# #     save_tts_history(text)

# if __name__ == "__main__":
#     while True:
#         user_text = input("\nEnter English text (or 'exit'): ")

#         if user_text.lower() == "exit":
#             break

#         text_to_speech(user_text)


TTS_HISTORY_FILE = "tts_history.txt"

from datetime import datetime
import pyttsx3

def save_tts_history(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(TTS_HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"Time: {timestamp}\n")
        f.write(f"Text Input (English): {text}\n")
        f.write("-" * 50 + "\n")


# Initialize TTS engine
# initially loads speech driver and voice database
tts_engine = pyttsx3.init()

# Force English voice
voices = tts_engine.getProperty("voices")
for voice in voices:
    if "english" in voice.name.lower():
        tts_engine.setProperty("voice", voice.id)
        break

tts_engine.setProperty("rate", 160)   # speaking speed
tts_engine.setProperty("volume", 1.0) # volume (0–1)

def text_to_speech(text):
    print("\n Speaking:")
    print(text)

    # Speak
    tts_engine.say(text)
    tts_engine.runAndWait()

    # Save history
    save_tts_history(text)   


if __name__ == "__main__":
    while True:
        user_text = input("\nEnter English text (or 'exit'): ")

        if user_text.lower() == "exit":
            break

        text_to_speech(user_text)  


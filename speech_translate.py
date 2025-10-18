import sounddevice as sd
import numpy as np
import whisper
from gtts import gTTS
from googletrans import Translator
import pygame
import tempfile
import os
import time

# ---------------------------
# Load Whisper model
# ---------------------------
print("⏳ Loading Whisper model (small)...")
model = whisper.load_model("small")
translator = Translator()
print("✅ Model loaded successfully.\n")

# ---------------------------
# Record audio from microphone
# ---------------------------
def record_audio(duration=5, samplerate=16000):
    print("🎙️ Recording started... Speak now!")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
    sd.wait()
    print("✅ Recording finished.")
    return np.squeeze(audio)

# ---------------------------
# Speak text safely and clearly
# ---------------------------
def speak(text, lang="en"):
    try:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tmp_path = tmp.name
        tmp.close()

        tts = gTTS(text=text, lang=lang)
        tts.save(tmp_path)

        # Wait until file is ready
        for _ in range(20):
            if os.path.exists(tmp_path) and os.path.getsize(tmp_path) > 100:
                break
            time.sleep(0.2)
        else:
            raise FileNotFoundError(f"❌ File not created: {tmp_path}")

        pygame.mixer.init()
        pygame.mixer.music.load(tmp_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.stop()
        pygame.mixer.quit()

        time.sleep(0.5)
        if os.path.exists(tmp_path):
            os.remove(tmp_path)

    except Exception as e:
        print(f"⚠️ Error during playback: {e}")

# ---------------------------
# Main loop
# ---------------------------
while True:
    print("\n🎧 Press Enter to speak or type 'exit' to quit.")
    cmd = input("> ").strip().lower()
    if cmd == "exit":
        print("🚪 Exiting...")
        break

    audio = record_audio(duration=5)

    print("🧠 Processing speech...")
    result = model.transcribe(audio)
    text_input = result["text"].strip()
    detected_lang = result.get("language", "unknown")

    if not text_input:
        print("❌ No speech detected.")
        continue

    print(f"🗣️ Detected Language: {detected_lang.upper()}")
    print(f"📝 Recognized text: {text_input}")

    try:
        if detected_lang == "ar":
            # Arabic → English
            text_translated = translator.translate(text_input, src="ar", dest="en").text
            print("🌍 English translation:", text_translated)
            speak(text_translated, "en")
        else:
            # English → Arabic
            text_translated = translator.translate(text_input, src="en", dest="ar").text
            print("🌍 Arabic translation:", text_translated)
            speak(text_translated, "ar")

    except Exception as e:
        print("⚠️ Error during translation or TTS:", e)
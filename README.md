# 🎙️ Speech + Face AI Toolkit

A complete toolkit that includes:
1. **Face Blur Detector** (OpenCV + Caffe)
2. **Arabic-to-English Speech Translator** (Whisper + gTTS)

---

## ⚙️ Installation

1️⃣ Clone or extract this folder  
2️⃣ Run the following command:
```bash
pip install -r requirements.txt
```

---

## 🧠 1. Face Blur Project


**Description:**  
Detects faces in an image and blurs them for privacy.

**Run Command:**
```bash
python face_blur.py
python live_face_blur.py

```

**Notes:**  
- Put your image in `example/5.jpeg`
- The blurred output will be saved as `example/output.jpg`

---

## 🎧 2. Speech Translator Project

**Description:**  
Records Arabic speech, transcribes it using Whisper, translates to English, and reads it aloud using gTTS.

**Run Command:**
```bash
python speech_translate.py
```

**Instructions:**
1. Press Enter to start.
2. Speak for 5 seconds.
3. Wait for the output text and spoken translation.
4. Type `exit` to quit.

---

## 🛠️ Troubleshooting
- If Whisper is slow, change the model name from `"small"` to `"tiny"`.
- Ensure your microphone works correctly.
- Requires internet for translation and speech synthesis.

---

## 👨‍💻 Author
Created by Abdulrahman  
Includes OpenCV Face Detection and Whisper-based Translation.

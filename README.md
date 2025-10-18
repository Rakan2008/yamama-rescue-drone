# 🚁 Yamama Rescue Drone – AI-Powered Emergency Detection System

> A fully integrated **AI and automation project** combining **n8n**, **OpenAI API**, and **Gmail**, along with **local AI modules** for face detection, speech translation, and onboard audio processing using **ReSpeaker Audio HAT**, to support smart rescue operations using drones.

---

## 🧭 Table of Contents
1. 🧩 Project Concept  
2. 🎯 Objectives  
3. ⚙️ Components & Technologies  
4. 🧠 System Overview  
5. 🔄 n8n Workflow  
6. 💾 Dashboard (Figma Design)  
7. 🎙️ Local AI Modules  
8. 🧠 AI Analysis Logic  
9. 🖼️ Hardware & Visuals  
10. ⚙️ Execution Steps  
11. 👨‍💻 Team Credits  

---

## 🧩 Project Concept

**Yamama Rescue Drone** is an intelligent system designed to enhance **search and rescue missions** using artificial intelligence.  
It captures aerial images via a Raspberry Pi camera, analyzes them using **OpenAI API** through **n8n**,  
and includes **local AI modules** that handle:
- Face detection and privacy blurring  
- Real-time Arabic-to-English voice translation  
- Audio input/output using **ReSpeaker Audio HAT**

---

## 🎯 Objectives

- Detect and classify emergency events (🔥 Fire, 🚑 Medical distress, 🩸 Bleeding).  
- Automate the process from **image capture → AI analysis → alert**.  
- Integrate **local AI processing** for face and speech recognition.  
- Provide **real-time audio feedback** through ReSpeaker HAT.  
- Support field operations with immediate, autonomous communication.  

---

## ⚙️ Components & Technologies

| Category | Tool / Device | Function |
|:--|:--|:--|
| 🔄 Automation | **n8n** | Automates AI workflows and email reporting. |
| 🤖 AI Engine | **OpenAI API** | Analyzes image content and generates structured reports. |
| 📧 Communication | **Gmail API** | Sends automatic alerts with detected results. |
| 💻 Processor | **Raspberry Pi 4** | Central control for local AI and sensors. |
| 📷 Imaging | **IMX477 HQ Camera** | Captures high-quality stills and video for AI analysis. |
| 🔊 Audio Module | **ReSpeaker Audio HAT** | Handles multi-microphone input and speaker output for translation. |
| 🧠 Local Vision | **OpenCV + Caffe** | Performs real-time face detection and blurring. |
| 🎙️ Audio AI | **Whisper + gTTS** | Performs Arabic-to-English speech translation. |
| 🚁 Drone Platform | **F450 Frame** | Main drone body with motor and flight control. |

---

## 🧠 System Overview

1️⃣ **Image Capture:**  
Drone camera captures frames during flight.  

2️⃣ **Cloud AI:**  
Images are sent to **n8n** → **OpenAI API** for deep scene analysis.  

3️⃣ **Local AI:**  
The Raspberry Pi runs **face detection**, **speech translation**, and **audio playback** using ReSpeaker.  

4️⃣ **Report Generation:**  
n8n prepares and emails a structured emergency report automatically.  

---

## 🔄 n8n Workflow

🧩 **Workflow Steps:**
1. **Execute Workflow** – Manual or automated trigger.  
2. **Edit Fields** – Upload or receive an image.  
3. **Analyze Image (OpenAI)** – AI vision analysis.  
4. **Code Node** – Formats output.  
5. **Build Report** – Generates a human-readable summary.  
6. **IF Conditions** – Classifies (🔥 Fire / 🚑 Injury / 🩸 Bleeding).  
7. **Merge + Gmail Nodes** – Sends the final email alert.  

📸 **n8n Workflow Preview:**  
![n8n Workflow](docs/images/n8n_workflow.png)

---

## 💾 Dashboard (Figma Design)

A **Figma-based Dashboard** visualizes:
- Live drone camera feed  
- AI analysis status and results  
- Detected events with visual indicators  
- Historical alert log  

📸 **Dashboard Preview:**  
![Dashboard Preview](docs/images/dashboard_figma.png)

---

## 🎙️ Local AI Modules

### 🧠 1. Face Blur Detection
Detects faces and automatically blurs them for privacy.

**Run Command:**
```bash
python face_blur.py
```

**Live Mode (Camera Stream):**
```bash
python live_face_blur.py
```

📝 Notes:
- Place an input image at `example/5.jpeg`  
- Output is saved as `example/output.jpg`  

---

### 🎧 2. Speech Translator (with ReSpeaker Audio HAT)
Records Arabic speech using **ReSpeaker HAT**, transcribes and translates it to English using **Whisper + OpenAI + gTTS**, and plays the translated result through the speaker.

**Run Command:**
```bash
python speech_translate.py
```

**How it works:**
1. Press Enter to start.  
2. Speak Arabic for 5 seconds through ReSpeaker mic.  
3. Whisper transcribes + OpenAI translates.  
4. gTTS generates English speech.  
5. Output is played via ReSpeaker speaker.  
6. Type `exit` to quit.  

---

## 🧠 AI Analysis Logic

- **OpenAI Vision API (via n8n)** analyzes the image, generates descriptive text, and classifies the scene.  
- **Local AI Modules** on Raspberry Pi handle face privacy and voice translation.  
- **ReSpeaker HAT** provides audio interface for real-time translation feedback.  
- The entire system functions seamlessly between **local edge AI** and **cloud intelligence**.  

---

## 🖼️ Hardware & Visuals

📷 **Camera IMX477 HQ**  
![Camera Module](docs/images/camera_imx477.jpg)

🧠 **Raspberry Pi 4**  
![Raspberry Pi 4](docs/images/raspberry_pi4.jpg)

🔊 **ReSpeaker Audio HAT**  
![ReSpeaker HAT](docs/images/respeaker_hat.jpg)

🚁 **F450 Drone Frame**  
![Drone F450](docs/images/drone_f450.jpg)

⚙️ **System in Action**  
![System Live](docs/images/system_live.jpg)

---

## ⚙️ Execution Steps

1️⃣ Connect Raspberry Pi, IMX477 Camera, and ReSpeaker Audio HAT.  
2️⃣ Run **local AI modules** for face and voice analysis.  
3️⃣ Start **n8n workflow** for image interpretation and alerting.  
4️⃣ Capture or upload an image.  
5️⃣ Wait for AI results (local + cloud).  
6️⃣ Check **Gmail inbox** for the report.  

---

## 👨‍💻 Team Credits

**Project Name:** Yamama Rescue Drone  
**Team Name:** Team Yamama  

| Role | Name |
|:--|:--|
| 👨‍🏫 Project Advisor / Mentor | **Mr. Badr** |
| 👥 Team Members | *(Add team names here, e.g., Ali, Nasser, Salem, etc.)* |
| 🧠 Technical Supervision | **Abdulrahman Alnashri** |

---

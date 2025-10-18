# 🚁 Yamama Rescue Drone – AI-Powered Emergency Detection System

> A fully integrated **AI and automation project** combining **n8n**, **OpenAI API**, and **Gmail**, along with **local AI modules** for face detection and real-time translation, to support smart rescue operations using drones.

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
It captures aerial images through a Raspberry Pi camera, analyzes them using **OpenAI API** through **n8n**,  
and also includes **local modules** that perform:
- Face detection and blurring for privacy  
- Real-time Arabic-to-English voice translation  

---

## 🎯 Objectives

- Detect and classify emergency events (🔥 Fire, 🚑 Medical distress, 🩸 Bleeding).  
- Automate the process from **image capture → AI analysis → alert**.  
- Enable **local AI** for offline functionality (face detection and translation).  
- Support field operations with immediate feedback.  

---

## ⚙️ Components & Technologies

| Category | Tool / Device | Function |
|:--|:--|:--|
| 🔄 Automation | **n8n** | Automates AI workflows and data handling. |
| 🤖 AI Engine | **OpenAI API** | Performs image analysis and report generation. |
| 📧 Communication | **Gmail API** | Sends automatic reports and alerts. |
| 💻 Processor | **Raspberry Pi 4** | Handles camera input and local AI scripts. |
| 📷 Imaging | **IMX477 HQ Camera** | Captures high-quality aerial images. |
| 🧠 Local Vision | **OpenCV + Caffe** | Detects and blurs faces for privacy. |
| 🎙️ Audio AI | **Whisper + gTTS** | Performs voice translation and text-to-speech. |
| 🚁 Drone Platform | **F450 Frame** | Physical drone body for flight and hardware mounting. |

---

## 🧠 System Overview

1️⃣ **Image Capture:**  
Drone camera captures frames during operation.  

2️⃣ **Cloud Analysis:**  
Images are sent to **n8n** → **OpenAI API** → analyzed for fire or distress.  

3️⃣ **Local AI Processing:**  
Parallel modules on Raspberry Pi perform **face detection** and **voice translation**.  

4️⃣ **Report Generation & Alert:**  
Results are formatted, summarized, and automatically emailed to the rescue team.

---

## 🔄 n8n Workflow

🧩 **Workflow Steps:**
1. **Execute Workflow** – Manual or automatic trigger.  
2. **Edit Fields** – Upload or receive an image.  
3. **Analyze Image (OpenAI)** – Uses AI vision to describe image content.  
4. **Code Node** – Formats structured text output.  
5. **Build Report** – Creates a readable emergency summary.  
6. **IF Conditions** – Filters (🔥 Fire / 🚑 Injury / 🩸 Bleeding).  
7. **Merge + Gmail Nodes** – Combines data and sends automatic email alerts.  

📸 **n8n Workflow Preview:**  
![n8n Workflow](docs/images/n8n_workflow.png)

---

## 💾 Dashboard (Figma Design)

A custom **Figma-based Dashboard** visualizes the system’s performance:  
- Displays live images from the drone.  
- Shows analysis progress and system status.  
- Highlights emergency detections with icons.  
- Lists recent alerts and email logs.

📸 **Dashboard Preview:**  
![Dashboard Preview](docs/images/dashboard_figma.png)

---

## 🎙️ Local AI Modules

The project includes **standalone Python scripts** for real-time operations that run directly on the Raspberry Pi or any local PC.

### 🧠 1. Face Blur Detection
Detects faces in an image and automatically blurs them for privacy.

**Run Command:**
```bash
python face_blur.py
```

**Live Mode (Camera Stream):**
```bash
python live_face_blur.py
```

📝 Notes:
- Place your input image in the folder `example/5.jpeg`  
- Output will be saved as `example/output.jpg`  

---

### 🎧 2. Speech Translator
Records Arabic speech, translates it into English using **Whisper + OpenAI + gTTS**, and plays back the result.

**Run Command:**
```bash
python speech_translate.py
```

**How it works:**
1. Press Enter to start.  
2. Speak Arabic for 5 seconds.  
3. Wait for transcription + translation.  
4. The system speaks the English translation out loud.  
5. Type `exit` to stop.  

---

## 🧠 AI Analysis Logic

The **OpenAI Vision API** inside **n8n** performs:
1. Textual description of the scene.  
2. Classification of potential hazards.  
3. Structured report generation.  
4. Automatic email notification.  

Local AI modules handle **face privacy** and **real-time speech translation**,  
while cloud AI handles **scene understanding** and **critical event detection**.

---

## 🖼️ Hardware & Visuals

📷 **Camera IMX477 HQ**  
![Camera Module](docs/images/camera_imx477.jpg)

🧠 **Raspberry Pi 4**  
![Raspberry Pi 4](docs/images/raspberry_pi4.jpg)

🚁 **F450 Drone Frame**  
![Drone F450](docs/images/drone_f450.jpg)

⚙️ **System in Action**  
![System Live](docs/images/system_live.jpg)

---

## ⚙️ Execution Steps

1️⃣ Connect the **Raspberry Pi** and camera module.  
2️⃣ Launch the **local AI modules** for face/speech analysis.  
3️⃣ Start the **n8n workflow** for cloud AI analysis.  
4️⃣ Capture or upload images to trigger detection.  
5️⃣ Wait for both local and cloud systems to finish analysis.  
6️⃣ Check your **email inbox** for the automated report.  

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

# 🎤 AI Voice Customer Support Agent (Gemini + Whisper + Gradio)

An intelligent voice-enabled customer support system powered by **Gemini 2.0 Flash**, **OpenAI Whisper**, and **gTTS**, built with a clean conversational UI using **Gradio** and fully deployed on **HuggingFace Spaces**.

This project allows users to speak or type queries, receive AI-generated responses, hear voice replies, and view full conversation history — all in a smooth, interactive interface.

---

## 🚀 Features

✅ Real-time **voice input** using OpenAI Whisper  
✅ Gemini-based conversational AI responses  
✅ **Text-to-Speech** output using gTTS  
✅ Clean multi-tab **Gradio interface**  
&nbsp;&nbsp;&nbsp;• API Key tab  
&nbsp;&nbsp;&nbsp;• Chat tab  
&nbsp;&nbsp;&nbsp;• History tab  
✅ Full conversation memory & history  
✅ Deployed on **HuggingFace Spaces**  
✅ Supports both text and voice conversations  
✅ Lightweight, fast, and easy to run

---

## 🌐 Live Demo (HuggingFace)

👉 **Try it here:**  
https://huggingface.co/spaces/johndonal/AI-Voice-Agent

No installation needed — everything runs in the cloud.

---

## 🧩 Tech Stack

- **Gemini 2.0 Flash** – AI conversation engine  
- **Whisper (base)** – Automatic Speech Recognition  
- **gTTS** – Neural voice generation  
- **Gradio** – Multi-tab UI  
- **Python** – Core logic  
- **HuggingFace Spaces** – Deployment platform  

---

## 🛠️ How It Works

The system uses a simple but powerful pipeline:

**Microphone / Text Input → Whisper (ASR) → Gemini Response → gTTS → Audio Output + Chat History**

- Whisper transcribes speech  
- Gemini generates a concise, professional, and humorous response  
- gTTS converts AI text into natural speech  
- Full conversation is stored and displayed in the History tab  

---

## 📂 Project Structure

```
AI-Voice-Agent/
│
├── app.py            # Main Gradio application (UI + logic)
├── model.py          # Gemini model configuration + response logic
├── sst.py            # Whisper speech-to-text module
├── tts.py            # gTTS text-to-speech module
├── requirements.txt  # Dependencies for HuggingFace or local run
└── README.md         # Documentation
```

---

## ▶️ Demo Preview

<p align="center">
  <a href="https://raw.githubusercontent.com/MuhammadMusabYaqoob/AI-Voice-Customer-Support-Agent/main/demo.mp4">
    <img src="https://img.shields.io/badge/▶️ Click_to_Watch_Demo-FF0000?style=for-the-badge" width="300"/>
  </a>
</p>

<p align="center">
  <video width="700" controls>
    <source src="https://raw.githubusercontent.com/MuhammadMusabYaqoob/AI-Voice-Customer-Support-Agent/main/demo.mp4" type="video/mp4">
  </video>
</p>

Use the following actions in the app:

1. Enter your **Gemini API Key**  
2. Open the **Chat** tab  
3. Record your voice OR type a message  
4. Listen to the AI’s audio reply  
5. View full conversation in the **History** tab  

Perfect for showing voice-based AI interactions in customer support use cases.

---

## 💡 Example Use-Cases

- Customer service automation  
- AI voice support demos  
- IVR-style automated phone systems  
- Smart assistants  
- Educational AI showcases  

---

## ⚙️ Installation (Run Locally)

```bash
git clone https://github.com/yourusername/AI-Voice-Agent
cd AI-Voice-Agent
pip install -r requirements.txt
python app.py
```

Make sure you add your:

```
GEMINI_API_KEY
```

before chatting.

---

## 🧑‍💻 Author

**Muhammad Musab**  
🌐 GitHub: https://github.com/muhammadmusabyaqoob  
📧 musabyaqoob2@gmail.com  

---

## 🏷️ Tags

`Gemini` `Whisper` `gTTS` `Gradio` `Speech Recognition` `Text-to-Speech` `AI Voice Agent` `Customer Support` `Automation` `HuggingFace`

---

## 🌟 Badges

![HuggingFace](https://img.shields.io/badge/Deploy-HuggingFace-blue?style=for-the-badge)
![Gemini](https://img.shields.io/badge/AI-Gemini%202.0%20Flash-yellow?style=for-the-badge)
![Whisper](https://img.shields.io/badge/ASR-Whisper-green?style=for-the-badge)
![Gradio](https://img.shields.io/badge/UI-Gradio-orange?style=for-the-badge)

# 🧠 AskMe – Offline Multilingual AI Chatbot

AskMe is a privacy-first, fully offline AI chatbot that runs local Large Language Models (LLMs) on your device using Ollama.  
It provides a WhatsApp-style chat interface and supports multilingual conversations without requiring internet access.

---

## 🚀 Features

- 💬 Chat-based UI using Streamlit
- 📴 Fully offline (no APIs)
- 🧠 Local LLM inference with Ollama
- 🌐 Multilingual support (English, Hindi, Telugu)
- 📂 Multi-session chat history
- 📥 Download chat conversations
- 🧠 Basic memory for user context
- ⚡ Optimized for low-RAM systems

---

## 🏗️ Tech Stack

| Component | Technology |
|-----------|------------|
Frontend | Streamlit |
Backend | Python |
LLM Runtime | Ollama |
Models | TinyLlama / Phi-2 / Gemma 2B |
Storage | JSON / SQLite |

---

## 🧩 Architecture

User → Streamlit UI → Python Backend → Ollama → Response → UI

---

## 📊 Performance (TinyLlama – 4GB RAM)

| Metric | Value |
|--------|-------|
Response Time | 1–2 seconds |
RAM Usage | ~3.5 GB |
Internet | Not required |

---

## 🔒 Privacy

- No cloud calls  
- No data tracking  
- All chats stored locally  
- 100% offline processing  

---

## 👨‍💻 Author

Keerthi Pulagala  
AI/ML Enthusiast | Offline AI Developer

# ⚙️ AskMe – Setup & Usage Guide

This file explains how to install, run, and use the AskMe offline chatbot.

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/AskMe.git
cd AskMe
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Install Ollama
Download from: https://ollama.com

Run a model:
```bash
ollama run tinyllama
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open in browser:  
http://localhost:8501

---

## 📄 How to Use

### Chat Mode
Type your message and get an instant offline response.

### PDF Question Answering (RAG)

1. Upload a PDF  
2. Ask questions like:  
   - “Summarize this document”  
   - “What are the key points?”  

The model answers using only the uploaded file.

---

## 🌍 Multilingual Example

User: నువ్వు ఎవరు?  
Bot: నేను AskMe – మీ ఆఫ్‌లైన్ AI సహాయకుడు.

---

## 📁 Project Structure

```
AskMe/
│── app.py
│── rag.py
│── memory.py
│── chat_history/
│── models/
│── requirements.txt
│── README_1.md
│── README_2.md
```

---

## 📜 License

MIT License

---

## ⭐ Resume Description

Developed AskMe, an offline multilingual AI chatbot using Ollama and TinyLlama with Streamlit UI, local PDF-based RAG using FAISS, chat memory, and multi-session history, running entirely without internet.

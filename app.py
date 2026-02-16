import streamlit as st
import subprocess
import uuid
import json
import os
import time

# ---------------- CONFIG ----------------
st.set_page_config(page_title="ASKME", page_icon="💬")
CHAT_DIR = "chats"
os.makedirs(CHAT_DIR, exist_ok=True)

# ---------------- FUNCTIONS ----------------
def run_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "tinyllama"],
        input=prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()

def typing_effect(text):
    placeholder = st.empty()
    output = ""
    for ch in text:
        output += ch
        placeholder.markdown(output)
        time.sleep(0.015)
    return output

def save_chat(chat_id, messages):
    with open(f"{CHAT_DIR}/{chat_id}.json", "w") as f:
        json.dump(messages, f, indent=2)

# ---------------- SESSION INIT ----------------
if "chat_id" not in st.session_state:
    st.session_state.chat_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ----------------
st.sidebar.title("📂 Chat Sessions")

if st.sidebar.button("➕ New Chat"):
    st.session_state.chat_id = str(uuid.uuid4())
    st.session_state.messages = []

for file in os.listdir(CHAT_DIR):
    if st.sidebar.button(file.replace(".json", "")):
        with open(f"{CHAT_DIR}/{file}", "r") as f:
            st.session_state.messages = json.load(f)
        st.session_state.chat_id = file.replace(".json", "")

# ---------------- UI ----------------
st.title("💬 KnowledgeBot (Offline AI)")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    # User message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    with st.chat_message("assistant"):
        response = run_ollama(user_input)
        animated = typing_effect(response)

    st.session_state.messages.append({"role": "assistant", "content": animated})

    save_chat(st.session_state.chat_id, st.session_state.messages)

# ---------------- DOWNLOAD ----------------
if st.session_state.messages:
    chat_text = "\n".join(
        [f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages]
    )

    st.download_button(
        "⬇ Download Conversation",
        chat_text,
        file_name="conversation.txt"
    )

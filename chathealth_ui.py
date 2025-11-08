import streamlit as st
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-flash-latest")

def chat_with_bot(msg):
    system_prompt = (
        "You are ChatHealth, a gentle virtual health assistant "
        "offering safe wellness tips and reminders to seek professional care."
    )
    prompt = f"{system_prompt}\n\nUser: {msg}"
    res = model.generate_content(prompt)
    return res.text.strip()

st.title("🩺 ChatHealth – Gemini AI Wellness Assistant")
st.caption("⚠️ ChatHealth gives general wellness info only, not medical diagnoses.")

if "history" not in st.session_state:
    st.session_state.history = []

for chat in st.session_state.history:
    st.chat_message(chat["role"]).write(chat["content"])

msg = st.chat_input("Ask a health question...")
if msg:
    st.chat_message("user").write(msg)
    reply = chat_with_bot(msg)
    st.chat_message("assistant").write(reply)
    st.session_state.history.append({"role": "user", "content": msg})
    st.session_state.history.append({"role": "assistant", "content": reply})

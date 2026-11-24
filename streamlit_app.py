import streamlit as st
import requests

st.set_page_config(page_title="VEZ", page_icon="🤖")

st.title("🤖 VEZ")
st.write("Assistente per la gestione delle schede rete")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

msg = st.chat_input("Scrivi un comando...")

if msg:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": msg
        }
    )

    try:

        r = requests.post(
            "https://carloferracini.pythonanywhere.com/vez",
            json={"message": msg},
            timeout=30
        )

        risposta = r.json().get("response")

except Exception as e:
    risposta = f"Errore: {e}"

if risposta:
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": risposta
        }
    )

   

    

    st.rerun()

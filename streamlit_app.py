import streamlit as st
import requests

st.set_page_config(page_title="VEZ", page_icon="🤖")

st.title("🤖 VEZ")

msg = st.chat_input("Scrivi un comando...")

if msg:

    st.chat_message("user").write(msg)

    try:

        r = requests.post(
            "https://carloferracini.pythonanywhere.com/vez",
            json={"message": msg},
            timeout=30
        )

        risposta = r.json()

        st.chat_message("assistant").write(
            risposta.get("response", "Nessuna risposta")
        )

    except Exception as e:

        st.chat_message("assistant").write(
            f"Errore: {e}"
        )

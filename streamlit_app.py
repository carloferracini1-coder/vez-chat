import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="VEZ",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 VEZ")
st.write("Assistente per la gestione delle schede rete")

# Aggiorna la pagina ogni 3 secondi
st_autorefresh(interval=3000, key="chatrefresh")

# Carica tutta la cronologia dal server
try:

    history = requests.get(
        "https://carloferracini.pythonanywhere.com/history",
        timeout=10
    ).json()

except Exception:

    history = []

# Visualizza la cronologia
for message in history:

    role = message.get("role", "assistant")
    user = message.get("user", "")

    content = message.get("content", "")

    with st.chat_message(role):

        if user and user != "VEZ":
            st.markdown(f"**{user}**")

        st.write(content)

# Campo nome utente
if "username" not in st.session_state:
    st.session_state.username = ""

username = st.sidebar.text_input(
    "Il tuo nome",
    value=st.session_state.username
)

st.session_state.username = username

# Nuovo messaggio
msg = st.chat_input("Scrivi un comando...")

if msg:

    try:

        requests.post(
            "https://carloferracini.pythonanywhere.com/vez",
            json={
                "message": msg,
                "user": username if username else "Anonimo"
            },
            timeout=30
        )

    except Exception as e:

        st.error(f"Errore: {e}")

    st.rerun()

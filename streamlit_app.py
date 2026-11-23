import streamlit as st

st.set_page_config(page_title="VEZ", page_icon="🤖")

st.title("🤖 VEZ")
st.write("Assistente per la gestione delle schede rete")

msg = st.chat_input("Scrivi un comando...")

if msg:
    st.chat_message("user").write(msg)

    st.chat_message("assistant").write(
        f"VEZ ha ricevuto: {msg}"
    )

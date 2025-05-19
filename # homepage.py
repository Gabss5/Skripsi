# homepage.py
import streamlit as st

st.set_page_config(page_title="Sentiment Analysis Google Playstore", layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### #flexiblesolutions")
    st.markdown("## Halo, selamat datang di sistem analisis sentimen aplikasi Google Playstore")
    st.markdown(
        "Lorem ipsum praesent ac massa at ligula reet est iaculis. "
        "Vivamus est mist aliquet elit ac nisl. "
        "Lorem ipsum praesent ac massa at ligula reet est iaculis. "
        "Vivamus est mist."
    )
    st.text_input("Silakan ketik aplikasi yang anda cari di bawah ini", placeholder="Contoh: YouTube")

with col2:
    st.image("g.png", width=300)  # pastikan file gambar g.png ada di folder yang sama


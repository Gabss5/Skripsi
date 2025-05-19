import streamlit as st
from PIL import Image

# Konfigurasi halaman
st.set_page_config(page_title="Analysis System", layout="wide")

# Gaya CSS untuk meniru desain dari gambar
st.markdown("""
    <style>
    body {
        background-color: #0D0225;
        color: white;
    }
    .main {
        background-color: #1B005E;
        padding: 3rem;
        border-radius: 25px;
    }
    .tag {
        background-color: #A29BFE;
        color: #0D0225;
        font-weight: bold;
        padding: 0.3rem 1rem;
        border-radius: 15px;
        display: inline-block;
        margin-bottom: 1rem;
    }
    .button-custom {
        background-color: white;
        color: black;
        border-radius: 25px;
        padding: 1rem;
        width: 100%;
        text-align: left;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='color:white;'>Analysis System.</h1>", unsafe_allow_html=True)
st.markdown("## Analysis Sentiment Apps Google Playstore")

# Layout 2 kolom
col1, col2 = st.columns([1.5, 1])

with col1:
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="tag">#flexiblesolutions</div>', unsafe_allow_html=True)
    st.markdown("### Halo, selamat datang di sistem analisis sentimen aplikasi Google Playstore")
    st.write("""
        Lorem ipsum praesent ac massa at ligula reet est iaculis. Vivamus est mist aliquet elit ac nisl. 
        Lorem ipsum praesent ac massa at ligula reet est iaculis. Vivamus est mist.
    """)
    app_name = st.text_input("Silakan ketik aplikasi yang ingin Anda cari", placeholder="contoh: com.google.android.youtube")
    if st.button("Cari Aplikasi"):
        st.markdwon(f"Anda mencari: {app_name}")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    image = Image.open("g.png")
    st.image(image, width=300)


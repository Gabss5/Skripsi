import streamlit as st
from transformers import pipeline

# Load model sentiment Bahasa Indonesia
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="w11wo/indonesian-roberta-base-sentiment-classifier")

classifier = load_model()

# UI
st.title("Analisis Sentimen Bahasa Indonesia 🇮🇩")
st.write("Masukkan teks ulasan di bawah ini:")

user_input = st.text_area("Teks Ulasan", height=150)

if st.button("Analisis"):
    if user_input.strip() == "":
        st.warning("Silakan masukkan teks terlebih dahulu.")
    else:
        prediction = classifier(user_input)[0]
        label = prediction['label']
        score = prediction['score']

        st.subheader("Hasil Analisis Sentimen:")
        st.markdown(f"**Label:** `{label}`")
        st.markdown(f"**Confidence Score:** `{score:.2f}`")

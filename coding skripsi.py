# --- STEP 1: Ambil Ulasan dari Google Play Store ---
from google_play_scraper import reviews
import pandas as pd

result, _ = reviews(
    'com.spotify.music',
    lang='id',
    country='id',
    count=500
)

df = pd.DataFrame(result)
df[['content', 'score']].to_csv('spotify_reviews.csv', index=False)


# --- STEP 2: Preprocessing Teks ---
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df = pd.read_csv('spotify_reviews.csv')
df['clean_content'] = df['content'].apply(clean_text)


# --- STEP 3: Analisis Sentimen dengan BERT ---
from transformers import pipeline

# Gunakan model sentiment yang sudah dilatih
classifier = pipeline("sentiment-analysis", model="w11wo/indonesian-bert-sentiment-classification")

# Prediksi sebagian data untuk ditampilkan
predictions = classifier(df['clean_content'].tolist()[:10])

for text, pred in zip(df['content'][:10], predictions):
    print(f"Ulasan: {text}\nPrediksi: {pred['label']} (score: {pred['score']:.2f})\n")


# --- STEP 4: Tambahkan Prediksi ke DataFrame & Visualisasi ---
df['sentiment'] = [p['label'] for p in classifier(df['clean_content'].tolist())]

import matplotlib.pyplot as plt

df['sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])
plt.title("Distribusi Sentimen Ulasan Spotify")
plt.xlabel("Sentimen")
plt.ylabel("Jumlah Ulasan")
plt.show()


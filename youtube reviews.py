from google_play_scraper import reviews
import pandas as pd

result, _ = reviews(
    'com.google.android.youtube',  # ID aplikasi YouTube
    lang='id',
    country='id',
    count=1000
)

df = pd.DataFrame(result)
df[['content', 'score']].to_csv('youtube_reviews.csv', index=False)
import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

df = pd.read_csv('youtube_reviews.csv')
df['clean_content'] = df['content'].apply(clean_text)
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="indobenchmark/indobert-base-p1")

results = classifier(df['clean_content'].tolist()[:1000])  # batasi untuk efisiensi

# Ambil label
df['sentiment'] = [res['label'] for res in results]
import matplotlib.pyplot as plt

# Hitung distribusi
df['sentiment'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])
plt.title("Distribusi Sentimen Ulasan YouTube")
plt.xlabel("Sentimen")
plt.ylabel("Jumlah Ulasan")
plt.show()
import seaborn as sns

plt.figure(figsize=(10,6))
sns.countplot(data=df, x='score', hue='sentiment', palette='Set2')
plt.title("Distribusi Sentimen Berdasarkan Rating Bintang")
plt.xlabel("Rating Bintang")
plt.ylabel("Jumlah Ulasan")
plt.legend(title="Sentimen")
plt.show()

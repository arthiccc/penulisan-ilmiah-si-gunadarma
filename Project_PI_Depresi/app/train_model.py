import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# 1. Dataset Lebih Luas (Bahasa Indonesia)
# 0: Normal/Positif, 1: Indikasi Depresi/Negatif
data = {
    'text': [
        # --- Kategori: Normal / Positif (0) ---
        'Saya merasa sangat bahagia hari ini dan bersemangat',
        'Hari yang cerah untuk berjalan-jalan di taman',
        'Terima kasih atas bantuan teman-teman semua',
        'Sangat senang bisa lulus ujian semester ini',
        'Makan siang hari ini sangat enak dan mengenyangkan',
        'Alhamdulillah, hidup saya terasa sangat berkah dan bahagia',
        'Saya bersyukur memiliki keluarga yang sangat mendukung',
        'Hari ini saya berhasil mencapai target pekerjaan saya',
        'Saya suka sekali membaca buku sambil minum kopi di sore hari',
        'Liburan kemarin sangat menyenangkan dan menyegarkan pikiran',
        'Semangat pagi! Mari kita jalani hari dengan penuh optimisme',
        'Menikmati waktu santai bersama anak dan istri di rumah',
        'Akhirnya bisa mencapai kebebasan finansial setelah kerja keras',
        'Hidup ini indah jika kita tahu cara bersyukur',
        'Senang sekali melihat kemajuan yang saya capai belakangan ini',
        'Hari yang luar biasa, penuh dengan tawa dan keceriaan',
        'Saya merasa damai dan tenang hari ini',
        'Bangga sekali dengan pencapaian tim kami bulan ini',
        'Olahraga pagi ini membuat tubuh saya terasa bugar',
        'Menghabiskan waktu dengan hobi favorit sangatlah menyenangkan',

        # --- Kategori: Indikasi Depresi / Negatif (1) ---
        'Saya merasa sangat sedih dan tidak punya harapan lagi',
        'Setiap hari terasa seperti beban yang sangat berat bagi saya',
        'Aku ingin tidur saja selamanya karena lelah dengan hidup ini',
        'Hati saya hancur dan tidak ada yang peduli pada saya',
        'Dunia terasa gelap dan saya merasa sendirian',
        'Saya sudah tidak sanggup lagi menghadapi masalah ini',
        'Rasanya ingin menyerah saja dari keadaan yang menyakitkan ini',
        'Saya merasa kosong dan hampa di dalam hati',
        'Tidak ada yang mengerti betapa beratnya beban yang saya pikul',
        'Sering merasa cemas dan gelisah tanpa alasan yang jelas',
        'Saya merasa tidak berguna dan hanya menjadi beban bagi orang lain',
        'Kehilangan minat pada hal-hal yang dulu saya sukai',
        'Terus menerus merasa lelah secara mental dan fisik',
        'Sulit sekali untuk bangun dari tempat tidur di pagi hari',
        'Saya merasa terisolasi dari dunia luar',
        'Pikiran buruk selalu menghantui saya setiap malam',
        'Saya merasa masa depan saya sangat suram dan tidak ada harapan',
        'Kenapa hidup ini begitu tidak adil dan menyakitkan?',
        'Saya merasa terjebak dalam lubang kegelapan yang dalam',
        'Menangis setiap malam tanpa tahu apa penyebab pastinya'
    ],
    'label': [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, # Label 0
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1  # Label 1
    ]
}

df = pd.DataFrame(data)

# 2. Preprocessing & Vectorization
# Ubah semua teks ke lowercase agar konsisten
df['text'] = df['text'].str.lower()

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])
y = df['label']

# 3. Training Model (Menggunakan smoothing alpha untuk dataset kecil)
model = MultinomialNB(alpha=0.1)
model.fit(X, y)

# 4. Save Model & Vectorizer
os.makedirs('model_assets', exist_ok=True)
joblib.dump(model, 'model_assets/sentiment_model.pkl')
joblib.dump(vectorizer, 'model_assets/vectorizer.pkl')

print("Model trained and saved successfully.")

# Outline Presentasi Sidang Penulisan Ilmiah
## Judul: Deteksi Dini Gejala Depresi menggunakan NLP berbasis Web

### Slide 1: Judul & Identitas
- Judul Proyek
- Nama Mahasiswa & NPM
- Nama Dosen Pembimbing

### Slide 2: Latar Belakang (The Problem)
- Urgensi: Peningkatan isu kesehatan mental secara global.
- Stigma: Hambatan akses ke bantuan profesional karena rasa malu/takut.
- Peluang: Pemanfaatan jejak digital/teks sebagai indikator kondisi psikologis.

### Slide 3: Masalah & Solusi
- **Masalah:** Deteksi dini seringkali terlambat karena kurangnya alat skrining yang privat dan instan.
- **Solusi:** Aplikasi "MindCheck" - Alat bantu skrining berbasis NLP yang anonim, mudah diakses, dan responsif.

### Slide 4: Landasan Teori (The Tech)
- **NLP (Natural Language Processing):** Cabang AI untuk interaksi komputer-manusia via teks.
- **TF-IDF:** Metode pembobotan kata berdasarkan tingkat kepentingannya.
- **Multinomial Naive Bayes:** Algoritma klasifikasi probabilistik yang sangat efisien untuk pemrosesan teks pendek.

### Slide 5: Alur Kerja Sistem (Flowchart)
- **Input:** Kalimat keluhan pengguna.
- **Preprocessing:** Case folding (penyeragaman huruf kecil) & Tokenisasi.
- **Vectorization:** Konversi teks ke angka (TF-IDF).
- **Classification:** Prediksi label (Normal vs Indikasi Depresi) menggunakan model Bayes.

### Slide 6: Demo Aplikasi & Case Study
- Simulasi input kalimat positif/normal.
- Simulasi input kalimat dengan indikasi depresi.
- **Highlight:** Kemampuan sistem menangani kalimat kompleks (Contoh: menangani konteks kebahagiaan finansial vs keluhan hidup).

### Slide 7: Evaluasi & Optimasi
- **Dataset:** Pengembangan dari dataset dasar ke dataset yang lebih variatif (40+ sampel kontekstual).
- **Tuning:** Penggunaan smoothing (Alpha 0.1) untuk meningkatkan sensitivitas terhadap kata-kata baru.
- **Performa:** Respon instan (< 500ms) dengan klasifikasi yang lebih akurat.

### Slide 8: Kesimpulan & Saran
- **Kesimpulan:** AI dapat digunakan sebagai "Early Warning System" kesehatan mental yang efektif.
- **Saran:** Integrasi dengan dataset medis yang lebih besar dan penggunaan model Deep Learning (seperti IndoBERT) untuk pengembangan selanjutnya.

### Slide 9: Penutup & Tanya Jawab (Q&A)
- Ucapan terima kasih.
- Sesi diskusi dengan Dosen Penguji.

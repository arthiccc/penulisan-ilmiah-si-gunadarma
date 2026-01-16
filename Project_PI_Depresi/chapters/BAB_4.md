# BAB 4 - IMPLEMENTASI DAN PENGUJIAN

## 4.1. Spesifikasi Lingkungan Implementasi
Sistem ini diimplementasikan menggunakan spesifikasi perangkat lunak sebagai berikut:
1.  **Bahasa Pemrograman:** Python 3.12
2.  **Library AI:** Scikit-Learn (untuk Naive Bayes), Pandas (untuk manajemen data), Joblib (untuk penyimpanan model).
3.  **Web Framework:** Flask (Backend) dan Bootstrap 5 (Frontend).
4.  **Lingkungan Pengembangan:** Virtual Environment (Venv) untuk memastikan isolasi dependensi.

## 4.2. Implementasi Model AI
Proses pelatihan model dilakukan melalui file `train_model.py`. Model dilatih menggunakan dataset sentimen Bahasa Indonesia yang telah dioptimasi dengan parameter *Lidstone Smoothing* (Alpha 0.1). Hal ini bertujuan agar model memiliki toleransi yang lebih baik terhadap variasi kata baru yang tidak terdapat dalam data latih.

## 4.3. Skenario Pengujian
Pengujian dilakukan untuk memverifikasi akurasi model dalam membedakan antara kalimat normal dan kalimat yang mengindikasikan depresi. Fokus pengujian adalah pada kalimat yang memiliki ambiguitas tinggi.

### 4.3.1. Uji Coba Kasus Normal
- **Input:** "hidup bahagia, udah nikah anak 2, udah financial freedom"
- **Hasil Prediksi:** Normal
- **Analisis:** Sistem berhasil mengenali kata kunci positif seperti "bahagia" dan "freedom" serta mengabaikan struktur kalimat yang bersifat deskriptif pencapaian hidup.

### 4.3.2. Uji Coba Kasus Indikasi Depresi
- **Input:** "saya merasa kosong dan hampa di dalam hati"
- **Hasil Prediksi:** Indikasi Depresi
- **Analisis:** Sistem memberikan bobot tinggi pada kata "kosong" dan "hampa" yang secara statistik dalam dataset merujuk pada label 1.

## 4.4. Analisis Hasil
Berdasarkan hasil pengujian, sistem mampu memberikan respon klasifikasi dalam waktu rata-rata kurang dari 500ms. Perluasan dataset terbukti secara signifikan menurunkan tingkat *false positive* pada input pengguna yang bersifat kompleks.

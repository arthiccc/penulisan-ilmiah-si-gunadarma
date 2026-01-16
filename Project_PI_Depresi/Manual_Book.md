# Manual Book: MindCheck Application
## Panduan Pengoperasian Aplikasi Deteksi Dini Gejala Depresi

### 1. Deskripsi Aplikasi
MindCheck adalah aplikasi berbasis web yang menggunakan Kecerdasan Buatan (AI) untuk menganalisis teks perasaan pengguna dan memberikan indikasi apakah teks tersebut menunjukkan gejala depresi atau normal.

### 2. Persyaratan Sistem
- Python 3.10 atau lebih baru.
- Koneksi internet (untuk memuat pustaka Bootstrap).
- Web Browser (Chrome, Firefox, atau Edge).

### 3. Instalasi (Untuk Pengembang)
1. Buka terminal atau command prompt.
2. Masuk ke folder `Project_PI_Depresi/app`.
3. Instal dependensi:
   ```bash
   pip install flask pandas scikit-learn joblib
   ```
4. Jalankan script pelatihan model (jika belum ada):
   ```bash
   python train_model.py
   ```
5. Jalankan aplikasi:
   ```bash
   python app.py
   ```

### 4. Cara Penggunaan
1. Akses aplikasi melalui browser di alamat `http://127.0.0.1:5000`.
2. Pada halaman utama, Anda akan melihat kotak teks (textarea).
3. Ketikkan apa yang Anda rasakan (minimal satu kalimat).
4. Klik tombol **"Analisis Sekarang"**.
5. Sistem akan menampilkan hasil analisis di bawah tombol.

### 5. Troubleshooting
- **Model not loaded properly:** Pastikan folder `model_assets` berisi file `.pkl` yang dihasilkan oleh `train_model.py`.
- **Server Error:** Periksa terminal untuk melihat detail error Python. Pastikan semua pustaka sudah terinstal.

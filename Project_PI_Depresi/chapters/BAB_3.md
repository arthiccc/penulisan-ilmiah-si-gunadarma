# BAB 3 - PEMBAHASAN

## 3.1. Arsitektur Sistem
Aplikasi "MindCheck" dibangun dengan arsitektur *Client-Server* sederhana yang efisien untuk pemrosesan teks *real-time*:
1.  **Frontend:** Menggunakan HTML5, CSS3 dengan kerangka kerja Bootstrap 5 untuk tampilan responsif, serta JavaScript (Fetch API) untuk mengirim data ke server tanpa memuat ulang halaman.
2.  **Backend:** Flask (Python) bertindak sebagai *Micro-framework* yang menyediakan *endpoint* API untuk menerima input teks dan mengembalikan hasil prediksi dalam format JSON.
3.  **Model AI:** Menggunakan algoritma *Multinomial Naive Bayes* yang diintegrasikan dengan pemrosesan *TF-IDF Vectorizer*. Model disimpan dalam format serialisasi (.pkl) menggunakan pustaka *joblib*.

## 3.2. Persiapan Data (Dataset) dan Preprocessing
Data yang digunakan untuk pelatihan model telah dikembangkan secara signifikan untuk meningkatkan akurasi klasifikasi. Dataset kini mencakup lebih dari 40 sampel kalimat Bahasa Indonesia yang dikelompokkan menjadi dua kategori:
-   **Label 0 (Normal):** Kalimat yang menunjukkan rasa syukur, pencapaian hidup (seperti pernikahan, anak, atau kesuksesan finansial), serta aktivitas sehari-hari yang positif.
-   **Label 1 (Indikasi Depresi):** Kalimat yang mencerminkan isolasi sosial, kelelahan mental kronis, kehilangan minat, hingga pikiran untuk menyakiti diri sendiri.

Tahapan **Preprocessing** yang diimplementasikan meliputi:
1.  **Case Folding:** Mengubah seluruh karakter teks menjadi huruf kecil (lowercase) agar model tidak membedakan bobot kata berdasarkan penggunaan huruf kapital (contoh: "Bahagia" dan "bahagia" dianggap sama).
2.  **Tokenisasi:** Pemecahan teks menjadi unit kata tunggal untuk analisis frekuensi.

## 3.3. Implementasi Algoritma dan Model Tuning
Proses klasifikasi menggunakan metode statistik berbasis probabilitas:
1.  **TF-IDF Vectorization:** Menghitung nilai kepentingan sebuah kata dalam dataset. Kata-kata unik yang spesifik pada label tertentu (seperti "hampa" atau "bersyukur") diberikan bobot lebih tinggi.
2.  **Smoothing (Lidstone Smoothing):** Penggunaan parameter **alpha = 0.1** pada model Naive Bayes. Hal ini dilakukan untuk menangani masalah kata-kata yang tidak muncul dalam data latih (*zero frequency problem*), sehingga model tetap mampu memberikan prediksi yang fleksibel terhadap variasi kalimat baru.

## 3.4. Antarmuka Aplikasi
Antarmuka dirancang dengan prinsip *User-Centered Design*. Fokus utama adalah memberikan pengalaman yang tenang dan tidak menghakimi. Hasil klasifikasi ditampilkan dengan indikasi warna (Hijau untuk Normal, Merah untuk Indikasi Depresi) guna memberikan isyarat visual yang mudah dipahami oleh pengguna.

## 3.5. Pengujian dan Hasil
Sistem diuji menggunakan skenario kalimat kompleks yang sebelumnya sering salah terklasifikasi (*false positive*). Sebagai contoh, kalimat **"hidup bahagia, udah nikah anak 2, udah financial freedom"** sekarang berhasil diklasifikasikan dengan benar sebagai **Normal** setelah adanya perluasan dataset dan optimasi parameter model. Kecepatan respon rata-rata sistem tetap terjaga di bawah 500ms.

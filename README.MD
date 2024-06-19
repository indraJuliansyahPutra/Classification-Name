# Klasifikasi Nama

Proyek ini menggunakan Streamlit untuk membuat aplikasi prediksi/klasifikasi Jenis Kelamin Seseorang berdasarkan masukan nama menggunakan Random Forest dan Naive Bayes. Dalam Project ini nama yang digunakan dalam pelatihan adalah nama orang Indonesia.

## Prasyarat

Pastikan Anda telah menginstal Docker di sistem Anda. Jika belum, Anda dapat mengunduh dan menginstalnya dari [sini](https://www.docker.com/get-started).

## Langkah-langkah untuk Menjalankan Proyek

1. Clone repositori ini:

   ```sh
   git clone https://github.com/username/klasifikasi-nama.git
   cd klasifikasi-nama
   ```

2. Build Docker image:

   ```sh
   docker build -t klasifikasi-nama .
   ```

3. Jalankan Docker container:

   ```sh
   docker run -p 8501:8501 klasifikasi-nama
   ```

4. Buka aplikasi di browser:

   ```sh
   Local URL: http://localhost:8501
   ```

## Proses Pengembangan

1. Pengumpulan Data:
   Data dikumpulkan dengan melakukan scraping di website Tanyanama.com menggunakan library Streamlit. Kode scraping tidak disertakan di repositori ini karena alasan hak cipta dan kebijakan penggunaan data.

2. Pengolahan Data:
   File data yang dikumpulkan digabungkan dan dilakukan penyesuaian format. Data yang dihasilkan relatif bersih, sehingga tidak memerlukan banyak proses pembersihan.

3. Pemodelan:
   Dua model machine learning digunakan untuk klasifikasi nama: Random Forest dan Naive Bayes. Kedua model ini dilatih dan disimpan di dalam folder masing-masing.

4. Pengembangan GUI:
   _User-Interface_ dibuat menggunakan Streamlit untuk memudahkan pengguna dalam melakukan prediksi nama.

5. Pembuatan Docker:
   Docker digunakan untuk mengemas aplikasi agar dapat dijalankan di berbagai lingkungan tanpa masalah dependensi.

## Deploy

Aplikasi ini juga telah dideploy melalui Streamlit dan dapat diakses melalui link berikut:
[https://gender-klasifikasi.streamlit.app/](https://gender-klasifikasi.streamlit.app/)

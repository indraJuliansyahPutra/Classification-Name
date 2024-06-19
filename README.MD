# Klasifikasi Nama

Proyek ini menggunakan Streamlit untuk membuat aplikasi prediksi berdasarkan model klasifikasi nama menggunakan Random Forest dan Naive Bayes.

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

# Gunakan image dasar Python
FROM python:3.9-slim

# Set lingkungan kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt .

# Instal dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh isi folder proyek ke dalam container
COPY . .

# Eksekusi Streamlit ketika container dijalankan
CMD ["streamlit", "run", "app.py"]

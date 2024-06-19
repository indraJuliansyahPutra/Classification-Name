import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Fungsi untuk memuat model dan vectorizer
def load_model_and_vectorizer(model_path):
    model = joblib.load(model_path)
    return model

# Fungsi untuk melakukan prediksi jenis kelamin
def predict_gender(names, model):
    predictions = model.predict(names)
    return predictions

# Fungsi utama untuk melakukan prediksi nama satu per satu
def main():
    # Path ke model yang sudah dilatih
    model_path = 'Naive Bayes\gender_classification_model.pkl'
    
    # Memuat model dan vectorizer
    model = load_model_and_vectorizer(model_path)
    
    # Input nama dari pengguna untuk diprediksi
    while True:
        name = input("Masukkan nama yang ingin diprediksi (atau ketik 'selesai' untuk berhenti): ")
        if name.lower() == 'selesai':
            break
        
        # Memastikan nama diinput dalam bentuk list
        names_to_predict = [name]
        
        # Lakukan prediksi
        predictions = predict_gender(names_to_predict, model)
        
        # Konversi hasil prediksi menjadi label
        gender_label = 'Perempuan' if predictions[0] == 0 else 'Laki-Laki'
        
        # Tampilkan hasil prediksi
        print(f'Nama: {name}, Prediksi Jenis Kelamin: {gender_label}')

# Memanggil fungsi main untuk melakukan prediksi
if __name__ == '__main__':
    main()

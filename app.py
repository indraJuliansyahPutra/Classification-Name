import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Fungsi untuk memuat model
def load_model(model_path):
    # Mengecek ekstensi file untuk menentukan jenis model
    if model_path.endswith('.pkl'):
        model = joblib.load(model_path)
    else:
        raise ValueError(f'Unsupported model format: {model_path}')
    return model

# Fungsi untuk melakukan prediksi jenis kelamin
def predict_gender(names, model):
    if isinstance(model, TfidfVectorizer):
        names_vec = model.transform(names)
        predictions = model.classifier.predict(names_vec)
    else:
        predictions = model.predict(names)
    return predictions

def main():
    st.title('Aplikasi Klasifikasi Jenis Kelamin berdasarkan Nama')
    menu = ['Home', 'Predict']
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Home')
        st.markdown("""
            Selamat datang di aplikasi ini! Silakan pilih menu 'Predict' untuk melakukan prediksi jenis kelamin berdasarkan nama.
            Gunakan model yang telah dilatih untuk memprediksi apakah nama yang dimasukkan adalah perempuan atau laki-laki.
        """)

    elif choice == 'Predict':
        st.subheader('Predict Jenis Kelamin')

        # Pilihan model
        model_type = st.selectbox('Pilih Model', ['Random Forest', 'Naive Bayes'])

        if model_type == 'Random Forest':
            model_path = 'Random Forest//rf.pkl'
        elif model_type == 'Naive Bayes':
            model_path = 'Naive Bayes//nb.pkl'

        # Memuat model
        model = load_model(model_path)

        # Input nama untuk diprediksi
        name = st.text_input('Masukkan nama untuk diprediksi:')
        if st.button('Prediksi'):
            if name.strip() == '':
                st.warning('Silakan masukkan nama terlebih dahulu.')
            else:
                # Memastikan nama diinput dalam bentuk list
                names_to_predict = [name]

                # Lakukan prediksi
                predictions = predict_gender(names_to_predict, model)

                # Konversi hasil prediksi menjadi label
                gender_label = 'Perempuan' if predictions[0] == 0 else 'Laki-Laki'

                # Tampilkan hasil prediksi dengan warna yang berbeda hanya untuk jenis kelamin
                if gender_label == 'Perempuan':
                    st.markdown(f'**Nama:**\n{name}\n\n**Prediksi Jenis Kelamin:** <span style="color: pink;">{gender_label}</span>', unsafe_allow_html=True)
                else:
                    st.markdown(f'**Nama:**\n{name}\n\n**Prediksi Jenis Kelamin:** <span style="color: green;">{gender_label}</span>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()

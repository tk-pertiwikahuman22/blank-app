import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Menampilkan Dataset dan Grafik dari 5 Kolom")

# Unggah file dataset
uploaded_file = st.file_uploader("Unggah file CSV", type="csv")

if uploaded_file is not None:
    # Baca dataset
    df = pd.read_csv(uploaded_file)

    # Tampilkan dataset
    st.write("Dataset:")
    st.write(df.head())  # Menampilkan 5 baris pertama

    # Pilih 5 kolom untuk ditampilkan dalam grafik
    selected_columns = st.multiselect("Pilih 5 Kolom untuk Grafik", df.columns, default=df.columns[:5])

    if len(selected_columns) == 5:
        # Tampilkan grafik garis untuk 5 kolom yang dipilih
        st.write("Grafik Line Chart:")
        st.line_chart(df[selected_columns])

        # Tampilkan grafik batang untuk 5 kolom yang dipilih
        st.write("Grafik Bar Chart:")
        st.bar_chart(df[selected_columns])
    else:
        st.write("Silakan pilih tepat 5 kolom.")
else:
    st.write("Silakan unggah file CSV untuk melanjutkan.")

import streamlit as st

st.title("VALUE BARANG TOKO")

Awal = st.number_input("jumlah Barang Awal", 0)
Masuk = st.number_input("Jumlah Barang Masuk", 0)
Keluar = st.number_input("Jumlah barang keluar", 0)
hitung = st.button("hitung value")

if hitung :
    jumlah = Awal + Masuk
    st.write ("Total barang masuk adalah", jumlah)

if hitung :
    jumlah = Awal + Masuk - Keluar
    st.write ("Total barang adalah", jumlah)
import streamlit as st

st.title("Bar Chart")
st.write("Kelompok 8")
st.markdown("""
    - Rehan Alamsyah Putra (0110222168)
    - M. Dzaky Dz.S (0110222187)
    - Ihwanul Fikri Ramadhan (0110222112)
""")

col1, col2 = st.columns(2)

col1.write("ini adalah kolom pertama")
col1.image("../../pertemuan1/assets/2.jpg", )

col2.write("ini adalah kelompok dua")
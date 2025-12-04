import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Bar Chart")
st.write("Kelompok 8")
st.markdown(
    """
    - Ihwanul Fikri Ramadhan 0110222112
    - Rehan Alamsyah Putra 0110222168
    - Muhammad Dzaky Dzulfikar Salim 0110222187


"""
)

# Data
data = {'Jurusan': ['Ilmu Komputer', 'Sistem Informasi', 'Teknik Informatika', 'Data Science'],
        'Jumlah Mahasiswa': [120, 150, 100, 90]
}

df = pd.DataFrame(data)

# Streamlit Bar Chart
st.title("Basic Bar Chart - Jumlah Mahasiswa PerJurusan")
st.bar_chart(df.set_index('Jurusan'))

# Bar chart menggunakan Matplotlib
st.title("Besic Bar Chart Menggunakan Matplotlib")
fig, ax = plt.subplots()
ax.bar(data['Jurusan'], data['Jumlah Mahasiswa'], color='skyblue')
ax.set_title('Jumlah Mahasiswa per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('Jumlah Mahasiswa')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)

#Data 2
st.title("Customized Basic Bar Chart")

fig, ax = plt.subplots()
colors = ["blue", "green", "orange", "purple"]
bars = ax.bar(data["Jurusan"], data["Jumlah Mahasiswa"], color=colors)
ax.set_title("Jumlah Mahasiswa per Jurusan")
ax.set_xlabel("Jurusan")
ax.set_ylabel("Jumlah Mahasiswa")

# Menambahkan nilai pada batang
for bar in bars:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
            str(int(bar.get_height())), ha='center', va='bottom')

st.pyplot(fig)
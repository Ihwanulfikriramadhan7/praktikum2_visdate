import streamlit as st
import pandas as pd
import numpy as np

st.title("Area Chart")
st.write("Kelompok 8")
st.markdown("""
    - Rehan Alamsyah Putra (0110222168)
    - M. Dzaky Dz.S (0110222187)
    - Ihwanul Fikri Ramadhan (0110222112)
""")

df = pd.DataFrame(
    np.random.randn(40,4),
    columns=["C1", "C2", "C3", "C4"]
)

st.area_chart(df)
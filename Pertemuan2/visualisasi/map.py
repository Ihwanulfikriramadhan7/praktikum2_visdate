import streamlit as st
import pandas as pd
import numpy as np 

st.title("Map")
st.write("Kelompok 8")
st.markdown("""
    - Rehan Alamsyah Putra (0110222168)
    - M. Dzaky Dz.S (0110222187)
    - Ihwanul Fikri Ramadhan (0110222112)
""")

df =  pd.DataFrame(
    np.random.randn(50,2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)
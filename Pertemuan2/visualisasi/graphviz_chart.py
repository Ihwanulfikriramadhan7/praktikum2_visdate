import streamlit as st
import graphviz as graphviz

st.title("Graphviz Chart")
st.write("Kelompok 8")
st.markdown("""
    - Rehan Alamsyah Putra (0110222168)
    - M. Dzaky Dz.S (0110222187)
    - Ihwanul Fikri Ramadhan (0110222112)
""")

st.graphviz_chart("""
    digraph {
         "Tranning Data" -> "ML Algorithn" 
         "ML Algorithn" -> "Model"
         "Model" -> "Results Forecasting"
            "New Data" -> "Model"       
        }

""")


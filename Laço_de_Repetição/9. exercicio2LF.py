import streamlit as st
import time

st.title("Números Pares")

if st.button("Iniciar"):
    for i in range(100, 121, 2):
        st.write(i)
        time.sleep(1)
    st.header("FIM")
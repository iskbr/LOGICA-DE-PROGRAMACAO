import streamlit as st
import time

st.title("Laço de repetição - FOR ")

st.header("Contagem de 1 a 10.")

if st.button("Iniciar"):
    for i in range(1,11):
        st.write(i)
        time.sleep(0.5)
    st.header("Fim.")
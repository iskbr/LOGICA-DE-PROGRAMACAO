import streamlit  as st
import time

st.title("Atividade 1")
st.write("Escrever um algoritmo que mostre os números ímpares entre 1 e 20")

if st.button("Iniciar"):
    for i in range(1, 21, 2):
        st.write(i)
        time.sleep(0.5)
    st.success("FIM")


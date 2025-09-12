import streamlit as st
import time

st.title("Laço de Repetção: For")
st.write("Escreva um algoritmo que solicite do usuário um número e mostre a tabuada de multiplicação do número informado.")

numero = st.number_input("Digite um número: ",min_value=1, step=1)


if st.button("Tabuada."):
    for i in range(1, 11, 1):
        resultado = numero * i
        st.write(f"{numero} x {i} = {resultado}")
    st.success("FIM.")
else:
    st.error("Por favor, digite um número.")
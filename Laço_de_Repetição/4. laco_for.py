import streamlit as st
import time

st.title("Soma.")
st.write("Escreva um Programa de computador que solicite do usuário 5 números inteiros e, ao final, apresente a soma de todos os números lidos.")

soma = 0 

for i in range(1,6):
    numero = st.number_input(f"Digite o {i}º número: ", step=1, min_value=0)
    soma = soma + numero
    

if st.button("Somar."):
    st.success(f"A soma dos números é: {soma}")
else:
    st.info("Informe os números.")


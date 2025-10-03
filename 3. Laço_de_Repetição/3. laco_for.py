import streamlit as st
import time

st.title("Laço de Repetição: For")
st.header("Contagem Regressiva.")
st.write("Escrever um algoritmo que solicite ao usuário um número e faça a contagem regressiva a partir do número informado até o número 1, aguardando um segundo para exibir cada número.")

numero = st.number_input("Digite o número: ", min_value=2, step=1)

if st.button("Iniciar"):
    for i in range(numero, 0, -1):
        st.warning(i)
        time.sleep(0.5)
    st.success("FIM")
else:
    st.error("Por favor, Digite um número.")

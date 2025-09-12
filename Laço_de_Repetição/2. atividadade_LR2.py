import streamlit as st

st.title("Boletim")

soma = 0

for i in range(4):
    nota = st.number_input(f"Digite a {i}° Nota: ", min_value=0)
    soma = soma + nota

media = soma / 4

if st.button("Mostrar resultado"):
    st.info(f"Média: {media}")
import streamlit as st

st.title("Média")

n1 = st.number_input("Digite sua primeira nota ", min_value=0, max_value=10, step=1)
n2 = st.number_input("Digite sua segunda nota ", min_value=0, max_value=10, step=1)

media = (n1 + n2) / 2

if st.button ("Verificar Média"):
    if media >= 7:
        st.success("Aprovado.")
    else:
        st.error("Reprovado.")
else:
    st.info("Por favor, digite suas notas.")
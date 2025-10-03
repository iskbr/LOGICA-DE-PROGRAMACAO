import streamlit as st

st.title("Boletim Final")
st.write("Solicite 3 notas e no final apresente a média e mostre se está aprovado, reprovado ou em recuperação.")

QUANTIDADE_NOTAS = 3 # Constante para dizer a quantidade de notas, q nunca vai mudar
soma = 0



for i in range(QUANTIDADE_NOTAS):
    nota = st.number_input(f"Digite a {i}° Nota: ", min_value=0)
    soma = soma + nota

media = soma / QUANTIDADE_NOTAS

if st.button("Mostrar resultado"):
    st.info(f"Média: {media}")
    if media >= 7:
        st.success("Aprovado")
    elif media < 4:
        st.error("Reprovado")
    else:
        st.warning("Em recuperação")

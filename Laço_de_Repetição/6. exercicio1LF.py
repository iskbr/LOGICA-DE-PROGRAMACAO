import streamlit as st

st.title("Exercicio 1")

n1 = st.number_input("Digite o primeiro número ", min_value=0, max_value=100, step=1)
n2 = st.number_input("Digite o segundo número ", min_value=0, max_value=100, step=1)

media = (n1 + n2) / 2
soma = n1 + n2
produto = n1 * n2
maior_numero = 0
menor_numero = 0
#st.write(f"A média: {media}")
#st.write(f"A soma: {soma}")
#st.write(f"O profuto: {produto}")


if st.button ("Verificar."):
    if n1 > n2:
        maior_numero = n1
        menor_numero = n2
    else:
        maior_numero = n2
        menor_numero = n1


st.write(f"A média: {media}")
st.write(f"A soma: {soma}")
st.write(f"O profuto: {produto}")
st.write(f"O maior número: {maior_numero}")
st.write(f"O menor número: {menor_numero}")

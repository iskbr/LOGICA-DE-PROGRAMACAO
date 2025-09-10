import streamlit as st

st.title("Idade")

idade = st.number_input("Digite sua idade", min_value=0, max_value=130, step=1)


if st.button("Verificar"):
    if idade < 18:
        st.write("Menor de idade.")
    else:
        st.write("Maior de idade.")

else:
    st.warning("Por favor, digite a idade.")


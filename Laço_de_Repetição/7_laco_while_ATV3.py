import streamlit as st

st.title("Login")
st.write("Crie um progrma que solicite ao usuário seu login e uma senha o programa deve continuar pedindo o login e a sneha até que ambos estejam corretos")

login_salvo = "Isaac"
senha_salva = "123"


login = st.text_input("Digite seu login:")
senha = st.text_input("Digite sua senha:", type="password")

if st.button("Verificar"):
    if senha == senha_salva and login == login_salvo:
        st.info("Entrando...")
    else:
        st.error("Login ou Senha inválidos.")

        
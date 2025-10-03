import streamlit as st

st.title("Faça o seu login")

login_salvo = "Isaac"
senha_salva = "123"

# Váriaveis internas do Streamlit
st.session_state.setdefault("campos", False)
st.session_state.setdefault("tentativas", 0)

login = st.text_input("Digite seu login:", disabled=st.session_state.campos)
senha = st.text_input("Digite sua senha:", type="password", disabled=st.session_state.campos)

if st.button("Verificar"):
        if senha == senha_salva and login == login_salvo:
            st.info("Entrando...")
        else:
            st.session_state.tentativas += 1
            if st.session_state.tentativas <= 3:
                st.warning(f"Login ou Senha inválidos, tentativas: {st.session_state.tentativas}")
            else:
                 st.session_state.campos = True
                 st.error("Número de tentativas inválida.")

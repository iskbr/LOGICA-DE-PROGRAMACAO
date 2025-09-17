import os
os.system("cls")

login_salvo = "isaac"
senha_salva = 123

for i in range(3):
    while True:
        login = input("Digite seu login: ")
        senha = int(input("Digite sua senha: "))
        if login_salvo == login and senha == senha_salva:
            print("Entrando...")
            break
        else:
            print("Login ou Senhas inválidos.")


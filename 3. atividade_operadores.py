import os
os.system("cls")

login = str (input("Digite o login: "))
senha = float (input("Digite a senha: "))

if login == "Isaac William" and senha == 12345:
    print("Bem-Vindo!")
else:
    print("Login ou senha inválidos.")
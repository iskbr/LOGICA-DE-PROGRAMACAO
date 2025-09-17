import os
os.system("cls")
#Crie um progrma que solicite ao usuário seu login e uma senha o programa deve continuar pedindo o login e a sneha até que ambos estejam corretos"


while True:
    login = str(input("Digite seu login:"))
    senha = int(input("Digite sua senha:"))
    if login == "Isaac" and senha == 123:
        print("Entrando.")
        break
    else:
        print("Login ou senha incorretos.")
    


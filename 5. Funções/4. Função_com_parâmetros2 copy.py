import os
os.system("cls")

# Criando uma função
# Função com passagem de parâmetros.
def saudacao(nome, idade):
    print(f"Olá, {nome}! Bem-vindo(a)!")
    print(f"Sua idade é {idade} anos.")

print("Solicitando Dados.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

# Chamando a função
saudacao(nome, idade)

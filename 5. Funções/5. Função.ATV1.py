import os
os.system("cls")

# Criando uma função
# Função com passagem de parâmetros.
def saudacao(nome, idade, peso, altura):
    print(f"Olá, {nome}! Bem-vindo(a)!")
    print(f"Sua idade é {idade} anos.")
    print(f"Seu peso é {peso}kg.")
    print(f"Sua altura é {altura} metros.")

print("Solicitando Dados.")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# Chamando a função
os.system("cls")
print("Dados.")
saudacao(nome, idade, peso, altura)

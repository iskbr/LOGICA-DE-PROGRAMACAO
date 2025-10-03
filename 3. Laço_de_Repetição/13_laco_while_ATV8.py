import os
os.system("cls")

soma = 0
quantidade_numeros = 0

while True:
    numero = int(input("Digite um número inteiro: "))
    
    quantidade_numeros += 1
    soma += numero
    if numero < 0:
        break

media = soma / quantidade_numeros

print(f"\n Sua média: {media:.2f}")
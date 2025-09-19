import os
os.system("cls")

soma_pares = 0
soma = 0
quantidade_numeros = 0
quantidade_pares = 0
quantidade_impares = 0

while True:
    numero = int(input("Digite um número inteiro: "))
        
    if numero %2 == 0:
        quantidade_pares += 1
        soma_pares += 1
    else:
        quantidade_impares += 1

    quantidade_numeros += 1
    soma += numero
    if numero == 0:
        break

media_pares = soma_pares / quantidade_pares
media = soma / quantidade_numeros

print(f"\nMédia total: {media:.2f}")
print(f"Média de pares:: {media_pares:.2f}")
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números impares: {quantidade_impares}")
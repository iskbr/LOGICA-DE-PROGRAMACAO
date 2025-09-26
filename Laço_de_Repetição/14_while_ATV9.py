import os
os.system("cls")

soma_pares = 0
soma = 0
quantidade_numeros = 0
quantidade_pares = 0
quantidade_impares = 0

while True:
    numero = int(input("Digite um número inteiro: "))
    if numero > 0:    
        if numero %2 == 0:
            quantidade_pares += 1
            soma_pares += 1
        else:
            quantidade_impares += 1

        quantidade_numeros += 1 #adicionar mais um ao contador
        soma += numero # Soma a nota atual ao valor da variável soma.
    
    if numero == 0:
        break

# Calculando
media_pares = soma_pares / quantidade_pares
media = soma / quantidade_numeros

#if quantidade_pares != 0:
#    media_pares = soma_pares / quantidade_pares
#else:
#    media_pares = 0
#
#if quantidade_numeros != 0:
#    media = soma / quantidade_numeros
#else:
#    media = 0

# Operação Ternária
media_pares = soma_pares / quantidade_pares if quantidade_pares != 0 else 0
media = soma / quantidade_numeros if quantidade_numeros != 0 else 0

print(f"\nMédia total: {media:.2f}")
print(f"Média de pares:: {media_pares:.2f}")
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números impares: {quantidade_impares}")
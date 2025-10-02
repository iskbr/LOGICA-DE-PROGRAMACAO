import os
os.system("cls")

lista_numeros = []

for i in range(5):
    numeros = float(input(f"Digite o {i+1}° número: "))
    lista_numeros.append(numeros)

for i in range(5):
    print(f"Números: {lista_numeros[i]}")

# menor = min(lista_numeros)
# maior = max(lista_numeros)

print(f"Maior número: {max(lista_numeros)}")
print(f"Menor número: {min(lista_numeros)}")

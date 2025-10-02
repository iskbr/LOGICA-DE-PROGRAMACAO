import os
os.system("cls")

lista_numeros = []
QUANTIDADES_DE_NUMEROS = 6
pares = 0
impares = 0

for i in range(QUANTIDADES_DE_NUMEROS):
    numeros = float(input(f"Digite o {i+1}° número: "))
    lista_numeros.append(numeros)
    if numeros % 2 == 0:
        pares += 1
    else:
        impares += 1


print("\n- Monstrando Resultados -")
# for i in range(QUANTIDADES_DE_NUMEROS):
#     print(f"{i+1}º Número: {lista_numeros[i]}")

#ForEach
for numeros in lista_numeros:
    print(f"Número: {numeros}")
print("\nInformando os números")
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")


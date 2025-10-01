import os
os.system("cls")

lista_notas = []

for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
media = soma / 3

# Mostras notas:
print("\n= Resultados =")
for i in range(3):
    print(f"Nota: {lista_notas[i]}")

print(f"Média: {media}")
print("FIM")
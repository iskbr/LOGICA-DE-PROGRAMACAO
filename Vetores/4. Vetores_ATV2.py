import os
os.system("cls")

lista_notas = []
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)
media = soma / QUANTIDADE_NOTAS

# Mostras notas:
print("\n= Resultados =")
for i in range(QUANTIDADE_NOTAS):
    print(f"Nota: {lista_notas[i]}")

print(f"Média: {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")
print("FIM")
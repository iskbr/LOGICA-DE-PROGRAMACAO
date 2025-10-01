import os
os.system("cls")

# Criando um Vetor (lista)
lista_notas = []

# Inserindo notas
for i in range(3):
    nota = int(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

soma = sum(lista_notas)

# Mostrar notas:
for i in range(3):
    print(f"Nota: {lista_notas[i]}")

print(f"Soma: {soma}")
print("FIM")
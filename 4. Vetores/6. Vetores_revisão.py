import os
os.system("cls")

# Criando um vetor.
vetor_de_notas = []

print("Solicitando 3 notas.")
for i in range(3):
    nota = float(input("Digite uma nota: "))
    # Inserindo uma nota na vetor de notas.
    vetor_de_notas.append(nota)

print("\nMostrando todas as notas.")
for i in range(3):
    # O valor da variável i começa zero.
    # O valor de i no vetor faz mostrar o índice no vetor.
    print(f"Nota: {vetor_de_notas[i]}")
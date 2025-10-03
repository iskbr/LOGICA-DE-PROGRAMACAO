import os
os.system("cls")

def positivo_negativo(valor):
    if valor > 0:
        print("Positivo")
    else:
        print("Negativo")

print("Solicitando Dados.")
valor = float(input("Digite um valor: "))

# Chamando a função.
positivo_negativo(valor)

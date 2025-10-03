import os
os.system("cls")


def resultado_tabuada(numero):
    for i in range(1, 10):
        print(f"{numero} x {i} = {numero * i}")

print("Solicitando resultados")
numero = float(input("Digite um número:"))

print("\nExibindo Resultados")
resultado_tabuada(numero)
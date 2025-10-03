import os
os.system("cls")

QUANTIDADE_VALORES = 5
valores = []

for i in range(QUANTIDADE_VALORES):
    valor = float(input(f"Digite o {i+1}º valor: "))
    if valor < 0:
        valor = 0
    valores.append(valor)

for i, valor in enumerate(valores, start=1):
    print(f"{i}º Valores: {valor}")

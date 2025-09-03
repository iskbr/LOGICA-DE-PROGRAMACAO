import os
os.system("cls")

macas = int (input("Digite a quantidade de maçãs desejada:"))


if macas < 12:
    preco = 1.30
elif macas >= 12:
    preco = 1.00

total = macas * preco

print(f"O valor total: {total:.1f}")


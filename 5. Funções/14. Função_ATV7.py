import os
os.system("cls")

def inflacao(n1):
    if n1 < 100:
        n1 = n1 * (1 + 0.10)
    else:
        n1 = n1 * (1 + 0.20)
    return n1

def resultado(preco_inflacionado):
    os.system("cls")
    print("==Resultado==")
    print(f"Valor inflacionado: {preco_inflacionado:.2f}R$")


preco = float(input("Digite o valor de um produto: "))
preco_inflacionado = inflacao(preco)

resultado(preco_inflacionado)
import os
os.system("cls")

n1 = int (input("Digite o primeiro número: "))
n2 = int (input("Digite o segundo número: "))
sinal = str (input("Digite a operação necessitada: "))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

match sinal:
    case "+":
        print(f"Resultado da soma: {soma}")
    case "-":
        print(f"Resultado da subtração: {subtracao}")
    case "*":
        print(f"Resultado da multiplicação: {multiplicacao}")
    case "/":
        print(f"Resultado da divisão: {divisao}")
    case _:
        print("Operação inválida.")
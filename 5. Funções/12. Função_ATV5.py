import os
os.system("cls")

def limpa_tela():
    os.system("cls")

def operacoes(n1,  n2):
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = n1 / n2 if n2 != 0 else "Divisão por zero!"
    return soma, subtracao, multiplicacao, divisao

def mostrar_resultados(soma, subtracao, multiplicacao, divisao):
    print("--Resultados--")
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")

limpa_tela()

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite um número: "))

resultado = operacoes(primeiro_numero, segundo_numero)

limpa_tela()
mostrar_resultados(*resultado)
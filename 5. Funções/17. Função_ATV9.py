import os
os.system("cls")

def calcular(n1, n2):
    imc = n1 / (n2 * n2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        print("Abaixo do peso. Consulte um nutricionista para orientação.")
    elif imc >= 18.5 and imc < 25:
        print("Peso normal. Mantenha hábitos saudáveis!")
    elif imc >= 25 and imc < 30:
        print("Sobrepeso. Considere uma dieta balanceada e atividade física.")
    elif imc >= 30 and imc < 35:
        print("Obesidade grau 1. Procure orientação de um profissional de saúde.")
    elif imc >= 35 and imc < 40:
        print("Obesidade grau 2. Consulte um médico para avaliação e orientação.")
    else:
        print("Obesidade grau 3. Busque assistência médica urgentemente.")

peso = float(input("Indique seu peso: "))
altura = float(input("Indique sua altura: "))

imc = calcular(peso, altura)
imc = classificar_imc(imc)

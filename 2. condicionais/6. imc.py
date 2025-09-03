import os
os.system("cls")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc < 18.6:
    print("Abaixo do peso.")
if imc >= 18.6 and imc < 25:
    print("Peso ideal (parabéns)")
if imc >= 25 and imc < 30:
    print("Acima do peso")
if imc >= 30 and imc < 35:
    print("Obesidade grau 1")
if imc >= 35 and imc < 40:
    print("Obesidade grau 2 (severa)")
if imc >= 40:
    print("Obesidade 3 (mórbida)")

print(f"Seu imc: {imc}")
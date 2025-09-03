import os
os.system("cls")

nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))

media = (nota1 + nota2) / 2

if media >= 6:
    print("Aprovado.")
else:
    print("Reprovado.")

if media >= 9:
    conceito = "A"
elif media >= 7 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
else:
    conceito = "E"


print(f"Sua média: {media}")
print(f"Seu Conceito: {conceito}")
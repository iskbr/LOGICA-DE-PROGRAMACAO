import os
os.system("cls")

while True:
    nota = float(input("Digite sua nota: "))
    if nota >= 0 and nota <= 10:
        break

print(f"Nota: {nota}")
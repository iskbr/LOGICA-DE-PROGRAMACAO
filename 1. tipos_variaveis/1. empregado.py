import os
os.system("cls")

codigo = int (input("Digite seu código: "))
idade = int (input("Digite sua idade: "))
trabalho = int (input("Digite o seu tempo de trabalho: "))

if idade >= 65 and trabalho >= 30:
    print("Requerer aposentadoria.")
else:
    print("Não requerer aposentadoria.")

print(f"Seu código: {codigo}")
print(f"Sua idade: {idade}")
print(f"Seu tempo de trabalho: {trabalho}")

import os
os.system("cls")
print("""
\t Opções para os sexos:
M - Masculino
F - Feminino

""")
sexo = str(input("Selecione seu sexo: "))
altura = float(input("Digite sua altura: "))
match sexo:
    case "M":
        print("Peso ideal.")
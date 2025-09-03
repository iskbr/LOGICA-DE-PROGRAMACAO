import os
os.system("cls")

print("""
Código \t Prato \t\t Valor
    1 \t Picanha \t R$25,00
    2 \t Lasanha \t R$20,00
    3 \t Strogonoff \t R$18,00
    4 \t Bife Acebolado  R$15,00
    5 \t Pão Com Ovo \t R$5,00

""")

codigo = int(input("Digite o código do prato desejado: "))

match codigo:
    case 1:
        print("Picanha / R$25,00")
    case 2:
        print("Lasanha / R$20,00")
    case 3:
        print("Strogonoff / R$18,00")
    case 4:
        print("Bife Acebolado / R$15,00")
    case 5:
        print("Pão com Ovo / R$5,00")
    case _:
        print("Código inválido.")
        
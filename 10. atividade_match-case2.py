import os
os.system("cls")


print("""
1 - Janeiro \t 7 - Julho
2 - Fevereiro \t 8 - Agosto
3 - Março \t 9 - Setembro
4 - Abril \t 10 - Outubro
5 - Maio \t 11 - Novembro
6 - Junho \t 12 - Dezembro

""")
mes = int(input("Digite o número indicando o mês do ano desejado:"))

match mes:
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Número Inválido.")

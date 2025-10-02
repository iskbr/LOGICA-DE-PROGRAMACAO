import os
os.system("cls")

lista_numeros = []
positivos = []
negativos = 0
QUANTIDADES_DE_NUMEROS = 5


for i in range(QUANTIDADES_DE_NUMEROS):
    numeros = float(input(f"Digite o {i+1}° número (negativo ou positivo):"))
    lista_numeros.append(numeros)

    if numeros < 0:
        negativos += 1
    elif numeros > 0:
        positivos.append(numeros)
    


print("= Mostrando Resultado =")
print(f"Quantidade de negativos: {negativos}")
print(f"Soma dos positivos {sum(positivos)}")
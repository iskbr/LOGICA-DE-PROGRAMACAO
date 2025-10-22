import os
os.system("cls")

lista_notas = []
QUANTIDADE_NOTAS = 3

def calcular_media(lista_notas):
    resultado = sum(lista_notas) / QUANTIDADE_NOTAS
    return resultado

for i in range(QUANTIDADE_NOTAS):
    notas = float(input(f"Escreva sua {i+1}º nota: "))
    lista_notas.append(notas)

media = calcular_media(lista_notas)

print("== Resultado ==")
print(f"Média: {media:.2f}")
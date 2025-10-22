import os
os.system("cls")

lista_notas = []
QUANTIDADE_NOTAS = 2

def calcular_media(lista_notas):
    resultado = sum(lista_notas) / QUANTIDADE_NOTAS
    return resultado

def resultado(media):
    os.system("cls")
    print("\t=== Resultados ===")
    if media >= 7:
        print("Aprovado.")
    else:
        print("Reprovado.")
    print(f"Média: {media}")

for i in range(QUANTIDADE_NOTAS):
    while True:
        notas = float(input(f"Digite a {i+1} nota:"))
        if notas >= 0 and notas <= 10:
            lista_notas.append(notas)
            break
        else:
            print("Erro, tente novamente...")

media = calcular_media(lista_notas)
resultado_final = resultado(media)

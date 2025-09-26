import os
os.system("cls")

# Determinando as váriaveis
qntd_notas = 0
soma = 0

while True:
    nota = float(input("Digite uma nota:"))
    
    qntd_notas += 1 #adicionar mais um ao contador
    soma += nota # Soma a nota atual ao valor da variável soma.

    resposta = input("Deseja adicionar mais uma nota?\n(Use S para sim, N para não)").upper()
    if resposta == "N":
        break

# Calculando média.
media = soma / qntd_notas

print(f"Sua média: {media:.2f}")
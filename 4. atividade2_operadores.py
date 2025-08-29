import os
os.system("cls")

idade = int (input("Digite sua idade: "))

if idade < 18 or idade > 65:
    print("Não é obrigatório votar.") 
else:
    print("É obrigatório o voto.")
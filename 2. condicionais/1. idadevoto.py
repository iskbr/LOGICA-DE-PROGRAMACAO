#Idades para voto.
import os
os.system("cls")

idade = int (input("Digite sua idade: "))


if idade < 16:
    print(f"Não pode votar.")
elif idade >= 16 and idade == 17:
    print(f"Voto opcional.")
elif idade >= 18 and idade < 65:
    print("Voto obrigatório.")
elif idade >= 65:
    print("Voto opcional.")


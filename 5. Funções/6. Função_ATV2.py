import os
os.system("cls")



def par_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

print("Solicitando Dados.")
numero = float(input("Digite um número: "))

# Chamando a função.
par_impar(numero)
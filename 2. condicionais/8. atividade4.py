import os
os.system("cls")

n1 = int (input("Digite o primeiro número inteiro: "))
n2 = int (input("Digite o segundo número inteiro: "))

media = (n1 + n2) / 2
soma = n1 + n2
produto = n1 * n2

print(f"Sua média: {media}")
print(f"Sua soma: {soma}")
print(f"Seu produto: {produto}")

if n1 < n2:
    print("O Primeiro número é o menor.")
elif n1 > n2:
    print("O primeiro número é maior.")
else:
    print("Os números são iguais.")



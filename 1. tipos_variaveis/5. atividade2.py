import os
os.system("cls")

n1 = float (input("Digite o primeiro número: "))
n2 = float (input("Digite o segundo número: "))

media = (n1 + n2) / 2
soma = n1 + n2
produto = n1 * n2

print(f"Sua média: {media}")
print(f"Sua soma: {soma}")
print(f"Seu produto: {produto}")

if n1 < n2:
    print("O Primeiro número é o menor.")
else:
    print("O Segundo número é o menor.")


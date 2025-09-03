import os
os.system("cls")

n1 = float (input("Digite o primeiro número: "))
n2 = float (input("Digite o segundo número: "))
n3 = float (input("Digite o terceiro número: "))

print(f"Primeiro número: {n1}")
print(f"Segundo número: {n2}")
print(f"Terceiro número: {n3}")

print(f"O maior número: {max(n1,n2,n3)}")
print(f"O menor número: {min(n1,n2,n3)}")

import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    idade: int
    peso: float
    altura: float

print("Solicitando os dados da pessoa.")
cliente1 = Cliente(nome=input("Digite seu nome:"), 
                   idade=int(input("Digite sua idade: ")), 
                   peso=float(input("Digite seu peso: ")), 
                   altura=float(input("Digite sua altura: ")))

os.system("cls")
print("=== Dados ===")
print(f"Nome: {cliente1.nome}\nIdade: {cliente1.idade}\nPeso: {cliente1.peso}\nAltura: {cliente1.altura}")


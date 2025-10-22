import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    cpf: int

@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

# Exemplo de uso da classe
pessoa1 = Pessoa("Alice", 30, 213412)
pet1 = Pet("Totó", 4, 8.4)

print("Exibindo dados da Pessoa")
print(f"Nome: {pessoa1.nome}\nIdade: {pessoa1.idade}\nCPF: {pessoa1.cpf}")
print()
print("Exibindo dados do Pet")
print(f"Nome: {pet1.nome}\nIdade: {pet1.idade}\nPeso: {pet1.peso}")
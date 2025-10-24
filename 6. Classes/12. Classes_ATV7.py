import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} Kg")
        print(f"Altura: {self.altura} M\n")

lista_de_pessoas = []

for i in range(4):
    os.system("cls")
    pessoa = Pessoa(nome=input("Digite seu nome: "), 
                    idade=int(input("Digite sua idade:")), 
                    peso=float(input("Digite seu peso: ")), 
                    altura=float(input("Digite sua altura: ")))
    lista_de_pessoas.append(pessoa)

os.system("cls")
print("=== Exibindo dados ===")
for indice, pessoa in enumerate(lista_de_pessoas, start=1):
    print(f"-- Pessoa {indice} --")
    pessoa.exibir_dados()
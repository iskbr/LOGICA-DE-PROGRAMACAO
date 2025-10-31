import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco # Relacionamento com a classe Endereco

    def mostrar_dados(self):
        os.system("cls")
        print("== Exibindo Dados ==")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}")

pessoa1 = Pessoa(nome= input("Digite seu nome:"), 
                 idade= int(input("Digite sua idade:")), 
                 endereco= Endereco(logradouro= input("Digite seu logradouro: "), numero= int(input("Digite seu número: "))))

dados = pessoa1.mostrar_dados()
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
    endereco: Endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}")

pessoa1 = Pessoa(nome="Isaac", 
                 idade=16, 
                 endereco= Endereco(logradouro="Rua A", 
                                    numero=23))

print("= Mostrar dados do cliente =")
pessoa1.mostrar_dados()
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


pessoa1 = Pessoa(nome="Isaac", 
                 idade=16, 
                 endereco= Endereco(logradouro="Rua A", 
                                    numero=23))

print("= Mostrar dados do cliente =")
print(f"Nome: {pessoa1.nome}")
print(f"Endereço: {pessoa1.endereco.logradouro}")
print(f"Número: {pessoa1.endereco.numero}")
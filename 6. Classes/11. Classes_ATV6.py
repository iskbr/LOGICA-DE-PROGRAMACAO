import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: Endereco

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}")
        print(f"Cidade: {self.endereco.cidade}")

print("= Solicitando Dados =")
pessoa1 = Pessoa(nome=input("Digite seu nome:"), 
                 email=input("Digite seu e-mail:"), 
                 endereco=Endereco(logradouro=input("Digite o logradouro do seu endereço: "), 
                                   numero=int(input("Digite o número do seu endereço: ")), 
                                   cidade=input("Digite o nome de sua cidade: ")))

os.system("cls")
print("= Exibindo Dados =")
pessoa1.mostrar_dados()
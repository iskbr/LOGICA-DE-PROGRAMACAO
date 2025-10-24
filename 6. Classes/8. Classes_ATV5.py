import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    cpf: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}\n")

    def dados_sms_marketing(self):
        print(f"Telefone: {self.telefone}\n")

lista_de_pessoas = []

for i in range(3):
    os.system("cls")
    dados_pessoa = Pessoa(nome=input("Digite seu nome:"), 
                          cpf=input("Digite seu CPF: "), 
                          telefone=input("Digite seu Telefone: "))
    lista_de_pessoas.append(dados_pessoa)

os.system("cls")
print("= Exibindo dados gerais =\n")
    #for dados_pessoa in lista_de_pessoas:
    #    dados_pessoa.mostrar_dados()
    # Usando enumerate para numerar as pessoas
for indice, dados_pessoa in enumerate(lista_de_pessoas, start=1):
    print(f"--- Pessoa {indice} ---")
    dados_pessoa.mostrar_dados()

print("= Exibindo telefone =\n")
    #for dados_pessoa in lista_de_pessoas:
    #    dados_pessoa.dados_sms_marketing()
for indice, dados_pessoa in enumerate(lista_de_pessoas, start=1):
    print(f"--- Pessoa {indice} ---")
    dados_pessoa.dados_sms_marketing()
import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Pessoa_Composta:
    nome: str
    email: str
    endereco: str

    def mostrar_dados(self):
        os.system("cls")
        print("\t= Exibindo Dados =")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco}")

    def mostrar_somente_nome(self):
        print(f"Nome: {self.nome}")

lista_pessoa = []

for i in range(2):
    pessoa = Pessoa_Composta(nome=input("Digite seu nome:"), 
                             email=input("Digite seu e-mail:"), 
                             endereco=input("Digite seu endereço: "))
    # Adicionando todos os dados da pessoa na lista
    lista_pessoa.append(pessoa)

print("\n= Exibindo Dados =")
for pessoa in lista_pessoa:
    pessoa.mostrar_dados()

print("\n= Somente nomes =")
for pessoa in lista_pessoa:
    pessoa.mostrar_somente_nome()
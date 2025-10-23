import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_dados(self):
       os.system("cls")
       print(f"Nome: {self.nome}")
       print(f"Email: {self.email}")
       print(f"Telefone: {self.telefone}")
       print(f"Endereço: {self.endereco}") 


print("Solicitando dados.")
pessoa1 = Pessoa(nome=input("Digite seu nome: "), 
                 email=input("Informe seu e-mail: "), 
                 telefone=(input("Informe seu número de telefone: ")), 
                 endereco=input("Informe seu endereço: "))


print("== Exibindo os dados ==")
pessoa1.mostrar_dados()
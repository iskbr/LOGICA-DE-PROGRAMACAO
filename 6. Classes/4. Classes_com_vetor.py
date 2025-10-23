import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

    def mostrar_dados(self):
       os.system("cls")
       print(f"Nome: {self.nome}")
       print(f"Idade: {self.idade}")

pessoa1 = Pessoa(nome=input("Digite seu nome: "), 
                 idade=int(input("Informe seu e-mail: ")))

pessoa2 = Pessoa(nome=input("Digite seu nome: "), 
                 idade=int(input("Informe sua idade: ")))


print("== Exibindo os dados ==")
pessoa1.mostrar_dados()
pessoa2.mostrar_dados()
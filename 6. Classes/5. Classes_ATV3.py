import os
os.system("cls")

from dataclasses import dataclass

@dataclass
class AliExpress:
    nome: str
    email: str
    endereco: str

    def dados_entrega(self):
        os.system("cls")
        print("\t\tExibindo dados.")
        print("\tDados de entrega.")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")

    def dados_email_marketing(self):
        print()
        print("\tDados de Marketing.")
        print(f"Nome:{self.nome}")
        print(f"E-mail: {self.email}")

cliente1 = AliExpress(nome=input("Digite seu nome: "), 
                      email=input("Informe seu e-mail:"), 
                      endereco=input("Informe seu endereço: "))

cliente1.dados_entrega()
cliente1.dados_email_marketing()
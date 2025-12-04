import os
import time
from dataclasses import dataclass

os.system("cls || clear")

lista_clientes = []
lista_produto = []

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: int
    endereco: str

    def mostrar_dados_clientes(self):
        print("\n-- Dados Pessoais --")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

@dataclass
class Produto:
    nome: str
    quantidade: int
    lote: str
    validade: str

    def mostrar_dados_produto(self):
        print("\n-- Dados do Produto --")
        print(f"Nome do Produto: {self.nome}")
        print(f"Quantidade do Produto: {self.quantidade}")
        print(f"Lote: {self.lote}")
        print(f"Validade: {self.validade}")

# Função auxiliar para verificar se a lista de cliente está vazia
def lista_cliente_esta_vazia(lista):
    if not lista:
        print("\nNão há Clientes cadastrados.")
        return True
    return False

# Função auxiliar para verificar se a lista de produtos está vazia
def lista_produto_esta_vazia(lista):
    if not lista:
        print("\nNão há produto cadastrados.")
        return True
    return False

# Função para Adicionar Cliente
def adicionar_cliente(lista_clientes):
    print("\n=== Adicionar Novo Cliente ===")

    nome = input("Digite seu Nome: ")
    email = input("Digite seu E-mail: ")
    telefone = int(input("Digite seu Número: "))
    endereco = input("Digite o seu Endereço: ")

    
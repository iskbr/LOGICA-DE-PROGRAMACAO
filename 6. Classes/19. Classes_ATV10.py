import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    data_de_admissao: str
    matricula: str
    endereco: str

@dataclass
class Cliente:
    nome: str
    data_de_nascimento: str
    endereco_cliente: str

lista_funcionario = []
QUANTIDADE_FUNCIONARIOS = 1
lista_cliente = []
QUANTIDADE_CLIENTES = 1

# Solicitando Dados dos funcionarios
print("== Solicitando Dados dos funcionarios ==")
for i in range(QUANTIDADE_FUNCIONARIOS):
    funcionario = Funcionario(nome=input("Digite seu Nome: "), 
                              data_de_admissao=input("Digite sua Data de Admissão: "), 
                              matricula=input("Digite sua Matrícula:"), 
                              endereco=input("Digite seu Endereço: "))
    lista_funcionario.append(funcionario) # Recebendo os dados da váriavel "funcionario" e colocando na lista

# Criando e salvando os dados dos funcionarios no arquivo dos funcionarios
nome_do_arquivo1 = "Funcionarios.csv" 

with open(nome_do_arquivo1, "a") as arquivo_funcionarios:
    for funcionario in lista_funcionario:
        arquivo_funcionarios.write(f"{funcionario.nome}, {funcionario.data_de_admissao}, {funcionario.matricula}, {funcionario.endereco}\n")
    print("\nDados dos funcionarios Salvos com Sucesso")


# Solicitando os dados dos clientes
print("\n== Solicitando dados dos Clientes ==")
for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(nome=input("Digite seu Nome: "), 
                              data_de_nascimento=input("Digite sua Data de Nascimento: "), 
                              endereco_cliente=input("Digite seu Endereço: "))
    lista_cliente.append(cliente) # Recebendo os dados e mandando para a lista dos clientes

# Criando e salvando os dados dos clientes
nome_do_arquivo2 = "Clientes.csv"

with open(nome_do_arquivo2, "a") as arquivo_clientes:
    for cliente in lista_cliente:
        arquivo_clientes.write(f"{cliente.nome}, {cliente.data_de_nascimento}, {cliente.endereco_cliente}\n")
    print("\nDados dos clientes Salvos com Sucesso")

print("\n== Exibindo dados dos Funcionários ==")
lista_exibir_funcionarios = []
try:
    with open(nome_do_arquivo1, "r") as arquivo_exibir_funcionario:
        lista_exibir_funcionarios = arquivo_exibir_funcionario.readlines()
        for funcionario in lista_exibir_funcionarios:
            print(f"-{funcionario.strip()}")
except FileNotFoundError:
    print("O arquivo dos Funcionários não foi encontrado.")

print("\n== Exibindo dados dos Clientes ==")
lista_exibir_clientes = []
try:
    with open(nome_do_arquivo2, "r") as arquivo_exibir_clientes:
        lista_exibir_clientes = arquivo_exibir_clientes.readlines()
        for cliente in lista_exibir_clientes:
            print(f"-{cliente.strip()}")
except FileNotFoundError:
    print("O arquivo dos Clientes não foi encontrado.")
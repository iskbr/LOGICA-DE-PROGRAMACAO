# import os
# os.system("cls")
# from dataclasses import dataclass

# @dataclass
# class Funcionario:
#     nome: str
#     data_de_nascimento: str
#     rg: str
#     cpf: str

#     def exibir_dados(self):
#         print(f"Nome: {self.nome}, Data de Nascimento: {self.data_de_nascimento}, RG: {self.rg}, CPF {self.cpf}\n")


# lista_de_funcionarios = []
# QUANTIDADE_FUNCIONARIOS = 2

# for i in range(QUANTIDADE_FUNCIONARIOS):
#     funcionario = Funcionario(nome=input("Digite seu nome: "), 
#                               data_de_nascimento=input("Digite sua Data de Nascimento: "), 
#                               rg=input("Digite seu RG:"), 
#                               cpf=input("Digite seu CPF: "))        
#     lista_de_funcionarios.append(funcionario)
#     print()

# nome_do_arquivo = "Funcionarios.csv"
# with open(nome_do_arquivo, "a") as arquivo_funcionarios:
#     for funcionario in lista_de_funcionarios:
#         arquivo_funcionarios.write(f"{funcionario.nome}, {funcionario.data_de_nascimento}, {funcionario.rg}, {funcionario.cpf}")
#     print("Dados salvos com sucesso.")
    
# print("\n== Exibindo todos os Funcionários ==")
# lista = []
# # Serve para não travar seu código quando um arquivo der 
# # try:
# #     with open(nome_do_arquivo, "r") as arquivo:
# #         lista_de_funcionarios = arquivo.readlines()
# #         nome, nascimento, rg, cpf = funcionario.strip().split(",")
# #         dados_funcionario = Funcionario(nome=nome, data_de_nascimento=nascimento, rg=rg, cpf=cpf)
# #         lista.append(dados_funcionario)
# #     for funcionario in lista:
# #         funcionario.exibir_dados()
# try:
#     with open(nome_do_arquivo, "r") as arquivo:
#         # CORREÇÃO 2: Adicionado () no readlines
#         linhas = arquivo.readlines() 
        
#         # CORREÇÃO 3: Adicionado um Loop para percorrer as linhas
#         for linha in linhas:
#             # Usamos 'linha' (texto) e não 'funcionario' (objeto)
#             # O if linha.strip() evita erros se houver linhas vazias no final
#             if linha.strip(): 
#                 nome, nascimento, rg, cpf = linha.strip().split(",")
                
#                 dados_funcionario = Funcionario(
#                     nome=nome, 
#                     data_de_nascimento=nascimento, 
#                     rg=rg, 
#                     cpf=cpf
#                 )
#                 lista.append(dados_funcionario)

#     # Exibindo os objetos criados a partir do arquivo
#     for func in lista:
#         func.exibir_dados()

# except FileNotFoundError:
#     print("O arquivo não foi encontrado.")


import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Funcionario:
    nome: str
    data_de_nascimento: str
    rg: str
    cpf: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Data de Nascimento: {self.data_de_nascimento}, RG: {self.rg}, CPF: {self.cpf}")

lista_de_funcionarios = []
QUANTIDADE_FUNCIONARIOS = 2

# --- CADASTRO ---
for i in range(QUANTIDADE_FUNCIONARIOS):
    print(f"\nCadastrando funcionário {i+1}:")
    funcionario = Funcionario(
        nome=input("Digite seu nome: "), 
        data_de_nascimento=input("Digite sua Data de Nascimento: "), 
        rg=input("Digite seu RG: "), 
        cpf=input("Digite seu CPF: ")
    )        
    lista_de_funcionarios.append(funcionario)

# --- SALVAR NO ARQUIVO ---
nome_do_arquivo = "Funcionarios.csv"

with open(nome_do_arquivo, "a") as arquivo_funcionarios:
    for funcionario in lista_de_funcionarios:
        # CORREÇÃO 1: Adicionado \n no final para pular linha
        arquivo_funcionarios.write(f"{funcionario.nome},{funcionario.data_de_nascimento},{funcionario.rg},{funcionario.cpf}\n")
    print("\nDados salvos com sucesso.")
    
print("\n== Exibindo todos os Funcionários (Lendo do Arquivo) ==")

lista_lida_do_arquivo = []

try:
    with open(nome_do_arquivo, "r") as arquivo:
        # CORREÇÃO 2: Adicionado () no readlines
        linhas = arquivo.readlines() 
        
        # CORREÇÃO 3: Adicionado um Loop para percorrer as linhas
        for linha in linhas:
            # Usamos 'linha' (texto) e não 'funcionario' (objeto)
            # O if linha.strip() evita erros se houver linhas vazias no final
            if linha.strip(): 
                nome, nascimento, rg, cpf = linha.strip().split(",")
                
                dados_funcionario = Funcionario(
                    nome=nome, 
                    data_de_nascimento=nascimento, 
                    rg=rg, 
                    cpf=cpf
                )
                lista_lida_do_arquivo.append(dados_funcionario)

    # Exibindo os objetos criados a partir do arquivo
    for func in lista_lida_do_arquivo:
        func.exibir_dados()

except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except ValueError:
    print("Erro ao ler os dados do arquivo. Verifique a formatação do CSV.")
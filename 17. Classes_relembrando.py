import os
os.system("cls")
from dataclasses import dataclass


@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float
    cpf: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura}, CPF: {self.cpf}\n\n")

lista_pacientes = []
QUANTIDADE_DE_PACIENTES = 1

for i in range(QUANTIDADE_DE_PACIENTES):
    paciente = Paciente(nome= input("Digite o seu nome: "), 
                        idade= int(input("Digite sua idade: ")), 
                        peso= int(input("Digite seu peso:")), 
                        altura=float(input("Digite sua altura:")), 
                        cpf= input("Digite seu CPF:")
                        )
    lista_pacientes.append(paciente)
    print()

#print("\nExibindo lista de pacientes:")
#for paciente in lista_pacientes:
    #paciente.exibir_dados()

# print("\nExibindo todo os pacientes:")
# try:
#     # "r" - read - leitura
#     with open(nome_do_arquivo, "r") as arquivo:
#         # Recebe todos os dados do arquivo de uma só vez.
#         lista_todos_pacientes = arquivo.readlines() # readlines é para ler todas as linhas do arquivo
#         for paciente in lista_todos_pacientes:
#             print(f'- {paciente.strip()}')

nome_do_arquivo = "dados_pacientes.csv"
    # "a" - append - gravar/acrescentar
with open(nome_do_arquivo, "a", encoding="uft-8") as arquivo_pacientes:
    for paciente in lista_pacientes:
        arquivo_pacientes.write(f"{paciente.nome}, {paciente.idade}, {paciente.peso}, {paciente.altura}, {paciente.cpf}\n")
        os.system("cls")
    print("Dados salvos com sucesso.")

print("\nExibindo todos os pacientes")
lista = []
try:
    # "r" - read - leitura
    with open(nome_do_arquivo, "r", encoding="uft-8") as arquivo:
        lista_todos_pacientes = arquivo.readlines
        nome,idade, peso, altura, cpf = paciente.strip().split(",")
        dados_paciente = Paciente(nome=nome, idade=int(idade), peso=float(peso), altura= float(altura), cpf=cpf)
        lista.append(dados_paciente)
    for paciente in lista:
        paciente.exibir_dados()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

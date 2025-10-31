import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str
    idade: int
    email: str
    telefone: str

    def exibir_dados(self):
        return f"{self.nome}, {self.idade}, {self.email}, {self.telefone}\n"

QUANTIDADE_ALUNOS = 2
lista_alunos = []

print("Solicitando dados do aluno.")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(nome=input("Digite seu nome: "), 
                  idade=int(input("Digite sua idade: ")), 
                  email=input("Digite seu email: "), 
                  telefone=str(input("Digite seu telefone: ")))
    lista_alunos.append(aluno)

print("\nSalvando Dados.")
arquivo = "dados_alunos.txt"

with open(arquivo, "a") as arquivo_alunos:
    for aluno in lista_alunos:
        arquivo_alunos.write(aluno.exibir_dados())
    print("Salvo com sucesso!")


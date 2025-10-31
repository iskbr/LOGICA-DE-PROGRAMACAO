import os
os.system("cls")
from dataclasses import dataclass

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def exibir_dados(self):
        return f"{self.nome}, {self.autor}, {self.categoria}, {self.preco}\n"

QUANTIDADE_LIVROS = 3
lista_livros = []

for i in range(QUANTIDADE_LIVROS):
    editora = Livro(nome=input("Digite o nome do livro: "), 
                    autor=input("Nome do autor: "), 
                    categoria=input("Categoria do livro: "), 
                    preco=float(input("Digite o preço: ")))
    lista_livros.append(editora)

nome_arquivo = "dados_livro.txt"

with open(nome_arquivo, "a") as arquivo:
    for editora in lista_livros:
        arquivo.write(editora.exibir_dados())
print("== Dados Salvos ==")
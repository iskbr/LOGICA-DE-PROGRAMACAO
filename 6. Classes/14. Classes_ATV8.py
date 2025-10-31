import os
os.system("cls")
from dataclasses import dataclass

@dataclass 
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

    def exibir_detalhes(self):
        os.system("cls")
        print(f"Título do Livro: {self.titulo}")
        print(f"Ano de publicação: {self.ano}")
        print(f"Autor: {self.autor.nome}")

editora = Livro(titulo= input("Digite o Título do Livro: "), 
                ano=int(input("Digite o ano de publicação: ")), 
                autor= Autor(nome= input("Nome do Autor: "), biografia= input("Sua Biografia: ")))

dados = editora.exibir_detalhes()
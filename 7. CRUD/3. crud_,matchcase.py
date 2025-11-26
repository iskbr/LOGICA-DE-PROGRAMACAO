import os
os.system("cls || clear")

# Criando uma lista
lista_clientes = []

# Create
print("CREATE - Adicionar / Inserir")
nome = input("Digite seu nome: ")
lista_clientes.append(nome)
print(f"O nome: {nome} foi inserido com sucesso!")

print("""
1 - Digitar um nome.
2 - Atualizar um nome.
3 - Deletar um nome.
""")

opcoes = int(input(""))
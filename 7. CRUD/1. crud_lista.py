import os
os.system("cls || clear")

# CRUD usando lista.
# Create = criar / salvar
# Read = buscar / selecionar
# Update = atualizar / modificar
# Delete = excluir

# Criando uma lista
lista_clientes = []

# Create
print("CREATE - Adicionar / Inserir")
nome = "Marta"
lista_clientes.append(nome)
print(f"O nome: {nome} foi inserido com sucesso!")

# READ
print("\nRead - Ler / Mostrar")
print(lista_clientes)

# UPDATE
print("\nUpdate - Atualizar / Alterar")
nome_para_atualizar = "Marta"
if nome_para_atualizar in lista_clientes:
    novo_nome = "Marta Silva"
    indice = lista_clientes.index(nome_para_atualizar) # indice é a posição dentro do vetor/lista || o index procura o nome e indica em qual indice ele está na lista
    lista_clientes[indice] = novo_nome
    print(f"O nome {nome_para_atualizar} foi atualizado para {novo_nome}.")
else:
    print(f"O nome {nome_para_atualizar} não foi encontrado.")

print(lista_clientes)

# DELETE
print("\nDelete - Excluir / Remover")
nome_para_excluir = "Marta"
if nome_para_excluir in lista_clientes:
    lista_clientes.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluído com sucesso!")
else:
    print(f"O nome {nome_para_excluir} não foi encontro.")

print(lista_clientes)
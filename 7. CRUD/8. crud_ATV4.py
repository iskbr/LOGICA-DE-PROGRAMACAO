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

# Função auxiliar para verificar se a lista de cliente está vazia
def lista_cliente_esta_vazia(lista):
    if not lista:
        print("\nNão há Clientes cadastrados.")
        return True
    return False


# Função para Adicionar Cliente
def adicionar_cliente(lista_clientes):
    print("\n=== Adicionar Novo Cliente ===")
    nome = input("Digite seu Nome: ")
    email = input("Digite seu E-mail: ")
    telefone = int(input("Digite seu Número: "))
    endereco = input("Digite o seu Endereço: ")

    novo_cliente = Cliente(nome=nome, 
                           email=email, 
                           telefone=telefone, 
                           endereco=endereco)
    
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} cadastrado com sucesso!")

# Função para encontrar o cliente
def encontrar_cliente_por_nome(lista_clientes, nome_para_buscar_cliente):
    nome_para_buscar_cliente_lower = nome_para_buscar_cliente.lower()

    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_para_buscar_cliente_lower:
            return cliente
    return None

# Função para mostrar todos os clientes
def mostrar_todos_clientes(lista_clientes):
    if lista_cliente_esta_vazia(lista_clientes):
        return

    print("\n=== Lista de Clientes ===")
    for cliente in lista_clientes:
        cliente.mostrar_dados_clientes()

# Função para atualizar os dados do cliente
def atualizar_cliente(lista_clientes):
    if lista_cliente_esta_vazia(lista_clientes):
        return      
    
    mostrar_todos_clientes(lista_clientes) # Mostra todos os clientes para ajudar no processo
    print("\n=== Atualizar dados do Cliente ===")

    nome_para_buscar = input("\nDigite o NOME do cliente que deseja alterar: ")
    cliente_encontrado = encontrar_cliente_por_nome(lista_clientes, nome_para_buscar)

    if cliente_encontrado:
        print(f"\nCliente {cliente_encontrado.nome} encontrado.")
        print("Digite os novos dados ou pressione ENTER para manter o valor atual.")

        # --- Atualizando dados ---
        print(f"Nome atual: {cliente_encontrado.nome}")
        novo_nome = input("Digite o novo nome:")
        if novo_nome:
            cliente_encontrado.nome = novo_nome

        print(f"E-mail Atual: {cliente_encontrado.email} ")
        novo_email = input("Digite o novo E-mail: ")
        if novo_email:
            cliente_encontrado.email = novo_email
        
        print(f"Telefone Atual: {cliente_encontrado.telefone} ")
        novo_telefone = input("Digite o novo Telefone: ")
        if novo_telefone:
            cliente_encontrado.telefone = novo_telefone
        
        print(f"Endereço Atual: {cliente_encontrado.endereco} ")
        novo_endereco = input("Digite o novo Endereço: ")
        if novo_endereco:
            cliente_encontrado.endereco = novo_endereco

        print(f"\nDados do Cliente atualizados com Sucesso!")
    else:
        print(f"\nCliente com nome '{nome_para_buscar}' não encontrado.")
        
# Função para excluir o Cliente
def excluir_cliente(lista_clientes):
    if lista_cliente_esta_vazia(lista_clientes):
        return
    
    mostrar_todos_clientes(lista_clientes) # Mostra a lista de todos os clientes para ajudar
    
    nome_para_buscar = input("\nDigite o Nome do cliente que deseja excluir: ")

    cliente_para_remover = encontrar_cliente_por_nome(lista_clientes, nome_para_buscar)
    if cliente_para_remover:
        lista_clientes.remove(cliente_para_remover)
        print(f"\nCliente {cliente_para_remover.nome} excluído com sucesso! ")
    else:
        print(f"\nCliente com nome '{nome_para_buscar}' não encontrado.")

# ====================================== PRODUTO ============================================

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

# Função auxiliar para verificar se a lista de produtos está vazia
def lista_produto_esta_vazia(lista):
    if not lista:
        print("\nNão há produto cadastrados.")
        return True
    return False

# Função para Adicionar Produto
def adicionar_produto(lista_produto):
    print("\n=== Adicionar Novo Produto ===")
    nome = input("Digite seu Nome: ")
    quantidade = int(input("Digite a quantidade do Produto: "))
    lote = input("Digite o Lote: ")
    validade = input("Digite a validade: ")

    novo_produto = Produto(nome=nome, 
                           quantidade=quantidade, 
                           lote=lote, 
                           validade=validade)
    
    lista_produto.append(novo_produto)
    print(f"\nProduto {nome} cadastrado com sucesso!")

# Função para encontrar o produto
def encontrar_produto_por_nome(lista_produto, nome_para_buscar_produto):
    nome_para_buscar_produto_lower = nome_para_buscar_produto.lower()

    for produto in lista_produto:
        if produto.nome.lower() == nome_para_buscar_produto_lower:
            return produto
    return None

# Função para mostrar todos os Produtos
def mostrar_todos_produtos(lista_produto):
    if lista_produto_esta_vazia(lista_produto):
        return

    print("\n=== Lista de Clientes ===")
    for produto in lista_produto:
        produto.mostrar_dados_produto()
    
# Função para atualizar os dados do produto
def atualizar_produto(lista_produto):
    if lista_produto_esta_vazia(lista_produto):
        return      
    
    mostrar_todos_produtos(lista_produto) # Mostra todos os produtos para ajudar no processo
    print("\n=== Atualizar dados do Produto ===")

    nome_para_buscar = input("\nDigite o NOME do produto que deseja alterar: ")
    produto_encontrado = encontrar_produto_por_nome(lista_produto, nome_para_buscar)

    if produto_encontrado:
        print(f"\nProduto {produto_encontrado.nome} encontrado.")
        print("Digite os novos dados ou pressione ENTER para manter o valor atual.")

        # --- Atualizando dados ---
        print(f"Nome atual: {produto_encontrado.nome}")
        novo_nome = input("Digite o novo nome:")
        if novo_nome:
            produto_encontrado.nome = novo_nome

        print(f"Quantidade Atual: {produto_encontrado.quantidade} ")
        nova_quantidade = input("Digite a nova Quantidade: ")
        if nova_quantidade:
            produto_encontrado.quantidade = nova_quantidade
        
        print(f"Lote Atual: {produto_encontrado.lote} ")
        novo_lote = input("Digite o novo Lote: ")
        if novo_lote:
            produto_encontrado.lote = novo_lote
        
        print(f"Validade Atual: {produto_encontrado.validade} ")
        nova_validade = input("Digite a nova Validade: ")
        if nova_validade:
            produto_encontrado.validade = nova_validade

        print(f"\nDados do Produto atualizados com Sucesso!")
    else:
        print(f"\nProduto com nome '{nome_para_buscar}' não encontrado.")

# Função para excluir o Produto
def excluir_produto(lista_produto):
    if lista_produto_esta_vazia(lista_produto):
        return
    
    mostrar_todos_produtos(lista_produto) # Mostra a lista de todos os produtos para ajudar
    
    nome_para_buscar = input("\nDigite o NOME do produto que deseja excluir: ")

    produto_para_remover = encontrar_produto_por_nome(lista_produto, nome_para_buscar)
    if produto_para_remover:
        lista_produto.remove(produto_para_remover)
        print(f"\nProduto {produto_para_remover.nome} excluído com sucesso! ")
    else:
        print(f"\nProduto com nome '{nome_para_buscar}' não encontrado.")        

# Loop do Menu
while True:
    print("""
=== Sistema de Gestão de Clientes e Produtos ===
1 - Adicionar Cliente
2 - Mostrar Todos Clientes
3 - Atualizar Dados do Cliente
4 - Excluir Cliente
5 - Adicionar Produto
6 - Mostrar Todos Produtos
7 - Atualizar Dados do Produto
8 - Excluir Produto
0 - Sair
""")
    
    try:
        opcao_selecionada = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("\nEntrada Inválida. Digite um número inteiro.")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao_selecionada:
        case 1:
            adicionar_cliente(lista_clientes)
        case 2:
            mostrar_todos_clientes(lista_clientes)
        case 3:
            atualizar_cliente(lista_clientes)
        case 4:
            excluir_cliente(lista_clientes)
        case 5:
            adicionar_produto(lista_produto)
        case 6:
            mostrar_todos_produtos(lista_produto)
        case 7:
            atualizar_produto(lista_produto)
        case 8:
            excluir_produto(lista_produto)
        case 0:
            print("\nEncerrando Sistema...")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")

    if opcao_selecionada != 0:
        if opcao_selecionada == 1 or opcao_selecionada == 3 or opcao_selecionada == 4 or opcao_selecionada == 5 or opcao_selecionada == 7 or opcao_selecionada == 8:
            time.sleep(2)
        elif opcao_selecionada == 2 or opcao_selecionada == 6:
             input("\nPressione ENTER para voltar ao menu...")
        
        os.system("cls || clear")
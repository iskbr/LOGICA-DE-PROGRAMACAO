import os
import time
from dataclasses import dataclass

# Limpa o terminal (Windows ou Linux/Mac)
os.system("cls || clear")

lista_funcionarios = []

@dataclass
class Funcionario:
    nome: str
    data_nascimento: str
    cpf: str
    funcao: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        # 'Nasc' expandido para 'Data de Nascimento'
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"CPF: {self.cpf}")
        print(f"Função: {self.funcao}")
        print("-" * 30)

# Função auxiliar para verificar se a lista está vazia
def lista_esta_vazia(lista):
    if not lista:
        print("\nNão há funcionários cadastrados.")
        return True
    return False

def adicionar_funcionario(lista_funcionarios):
    print("\n=== Adicionar Novo Funcionário ===")
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (dia/mês/ano): ")
    cpf = input("Digite o CPF: ")
    funcao = input("Digite a função/cargo: ")

    novo_funcionario = Funcionario(
        nome=nome, 
        data_nascimento=data_nascimento, 
        cpf=cpf, 
        funcao=funcao
    )
    
    lista_funcionarios.append(novo_funcionario)
    print(f"\nFuncionário {nome} adicionado com sucesso!")

# Função para encontrar funcionário pelo NOME
def encontrar_funcionario_por_nome(lista_funcionarios, nome_para_buscar):
    nome_para_buscar_minusculo = nome_para_buscar.lower()
    
    # Variável 'func' alterada para 'funcionario' para evitar abreviação
    for funcionario in lista_funcionarios:
        if funcionario.nome.lower() == nome_para_buscar_minusculo:
            return funcionario
    return None

def mostrar_todos_funcionarios(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return
    
    print("\n=== Lista de Funcionários ===")
    # Variável 'func' alterada para 'funcionario'
    for funcionario in lista_funcionarios:
        funcionario.mostrar_dados()

def atualizar_funcionario(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return
    
    mostrar_todos_funcionarios(lista_funcionarios)
    print("=== Atualizar dados do Funcionário ===")
    
    nome_para_buscar = input("\nDigite o NOME do funcionário que deseja alterar: ")
    
    funcionario_encontrado = encontrar_funcionario_por_nome(lista_funcionarios, nome_para_buscar)

    if funcionario_encontrado:
        print(f"\nFuncionário {funcionario_encontrado.nome} encontrado.")
        print("Digite os novos dados ou pressione ENTER para manter o valor atual.")

        print(f"\nNome atual: {funcionario_encontrado.nome}")
        novo_nome = input("Novo nome: ")
        if novo_nome:
            funcionario_encontrado.nome = novo_nome

        print(f"\nData de Nascimento atual: {funcionario_encontrado.data_nascimento}")
        nova_data_nascimento = input("Nova data de nascimento: ")
        if nova_data_nascimento:
            funcionario_encontrado.data_nascimento = nova_data_nascimento

        print(f"\nCPF atual: {funcionario_encontrado.cpf}")
        novo_cpf = input("Novo CPF: ")
        if novo_cpf:
            funcionario_encontrado.cpf = novo_cpf

        print(f"\nFunção atual: {funcionario_encontrado.funcao}")
        nova_funcao = input("Nova função: ")
        if nova_funcao:
            funcionario_encontrado.funcao = nova_funcao

        print(f"\nDados atualizados com sucesso!")
    else:
        print(f"\nFuncionário com nome '{nome_para_buscar}' não encontrado.")

def excluir_funcionario(lista_funcionarios):
    if lista_esta_vazia(lista_funcionarios):
        return
    
    mostrar_todos_funcionarios(lista_funcionarios)
    
    nome_para_buscar = input("\nDigite o NOME do funcionário que deseja excluir: ")

    funcionario_para_remover = encontrar_funcionario_por_nome(lista_funcionarios, nome_para_buscar)

    if funcionario_para_remover:
        lista_funcionarios.remove(funcionario_para_remover)
        print(f"\nFuncionário {funcionario_para_remover.nome} excluído com sucesso!")
    else:
        print(f"\nFuncionário com nome '{nome_para_buscar}' não encontrado.")

# Loop principal do Menu
while True:
    print("""
=== Sistema de RH - Gestão de Funcionários ===
1 - Adicionar Funcionário
2 - Mostrar Todos
3 - Atualizar Dados (Busca por Nome)
4 - Excluir Funcionário (Busca por Nome)
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
            adicionar_funcionario(lista_funcionarios)
        case 2:
            mostrar_todos_funcionarios(lista_funcionarios)
        case 3:
            atualizar_funcionario(lista_funcionarios)
        case 4:
            excluir_funcionario(lista_funcionarios)
        case 0:
            print("\nEncerrando sistema...")
            break
        case _:
            print("\nOpção inválida. Tente novamente.")

    if opcao_selecionada != 0:
        if opcao_selecionada == 1 or opcao_selecionada == 3 or opcao_selecionada == 4:
            time.sleep(2)
        elif opcao_selecionada == 2:
             input("\nPressione ENTER para voltar ao menu...")
        
        os.system("cls || clear")
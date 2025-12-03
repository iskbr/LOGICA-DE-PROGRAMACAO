import os
import time
from dataclasses import dataclass

# Limpa o terminal para iniciar
os.system("cls || clear")

lista_alunos = []

@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str
    estado: str

    # Método auxiliar para formatar o endereço em texto
    def obter_endereco_formatado(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}/{self.estado}"

@dataclass
class Aluno:
    nome: str
    data_nascimento: str
    registro_academico: str # Antigo R.A. (sem abreviações)
    curso: str
    endereco: Endereco # Aqui usamos a classe Endereco como um tipo de dado

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Data de Nascimento: {self.data_nascimento}")
        print(f"Registro Acadêmico (R.A.): {self.registro_academico}")
        print(f"Curso: {self.curso}")
        # Acessamos os dados da classe Endereco que está dentro do Aluno
        print(f"Endereço: {self.endereco.obter_endereco_formatado()}")
        print("-" * 40)

# Função auxiliar para verificar se a lista está vazia
def lista_esta_vazia(lista):
    if not lista:
        print("\nNão há alunos cadastrados.")
        return True
    return False

def adicionar_aluno(lista_alunos):
    print("\n=== Adicionar Novo Aluno ===")
    
    # Dados Pessoais
    print("-- Dados Pessoais --")
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento: ")
    registro_academico = input("Digite o R.A.: ")
    curso = input("Digite o curso: ")

    # Dados de Endereço
    print("\n-- Dados de Endereço --")
    logradouro = input("Digite o logradouro (Rua/Av): ")
    numero = input("Digite o número: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")

    # Primeiro criamos o objeto Endereço
    novo_endereco = Endereco(
        logradouro=logradouro,
        numero=numero,
        cidade=cidade,
        estado=estado)

    # Depois criamos o Aluno, passando o objeto endereço criado acima
    novo_aluno = Aluno(
        nome=nome,
        data_nascimento=data_nascimento,
        registro_academico=registro_academico,
        curso=curso,
        endereco=novo_endereco)
    
    lista_alunos.append(novo_aluno)
    print(f"\nAluno {nome} adicionado com sucesso!")

def encontrar_aluno_por_nome(lista_alunos, nome_para_buscar):
    nome_para_buscar_minusculo = nome_para_buscar.lower()
    
    for aluno in lista_alunos:
        if aluno.nome.lower() == nome_para_buscar_minusculo:
            return aluno
    return None

def mostrar_todos_alunos(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    
    print("\n=== Lista de Alunos ===")
    for aluno in lista_alunos:
        aluno.mostrar_dados()

def atualizar_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    
    mostrar_todos_alunos(lista_alunos)
    print("=== Atualizar dados do Aluno ===")
    
    nome_para_buscar = input("\nDigite o NOME do aluno que deseja alterar: ")
    
    aluno_encontrado = encontrar_aluno_por_nome(lista_alunos, nome_para_buscar)

    if aluno_encontrado:
        print(f"\nAluno {aluno_encontrado.nome} encontrado.")
        print("Digite os novos dados ou pressione ENTER para manter o valor atual.")

        # --- Atualizando Dados Pessoais ---
        print("\n--- Dados Pessoais ---")
        
        print(f"Nome atual: {aluno_encontrado.nome}")
        novo_nome = input("Novo nome: ")
        if novo_nome:
            aluno_encontrado.nome = novo_nome

        print(f"Data de Nascimento atual: {aluno_encontrado.data_nascimento}")
        nova_data = input("Nova data de nascimento: ")
        if nova_data:
            aluno_encontrado.data_nascimento = nova_data

        print(f"R.A. atual: {aluno_encontrado.registro_academico}")
        novo_registro = input("Novo R.A.: ")
        if novo_registro:
            aluno_encontrado.registro_academico = novo_registro

        print(f"Curso atual: {aluno_encontrado.curso}")
        novo_curso = input("Novo curso: ")
        if novo_curso:
            aluno_encontrado.curso = novo_curso

        # --- Atualizando Endereço ---
        print("\n--- Endereço ---")
        
        # Acessamos aluno_encontrado.endereco.logradouro
        print(f"Logradouro atual: {aluno_encontrado.endereco.logradouro}")
        novo_logradouro = input("Novo logradouro: ")
        if novo_logradouro:
            aluno_encontrado.endereco.logradouro = novo_logradouro

        print(f"Número atual: {aluno_encontrado.endereco.numero}")
        novo_numero = input("Novo número: ")
        if novo_numero:
            aluno_encontrado.endereco.numero = novo_numero

        print(f"Cidade atual: {aluno_encontrado.endereco.cidade}")
        nova_cidade = input("Nova cidade: ")
        if nova_cidade:
            aluno_encontrado.endereco.cidade = nova_cidade
            
        print(f"Estado atual: {aluno_encontrado.endereco.estado}")
        novo_estado = input("Novo estado: ")
        if novo_estado:
            aluno_encontrado.endereco.estado = novo_estado

        print(f"\nDados do aluno atualizados com sucesso!")
    else:
        print(f"\nAluno com nome '{nome_para_buscar}' não encontrado.")

def excluir_aluno(lista_alunos):
    if lista_esta_vazia(lista_alunos):
        return
    
    mostrar_todos_alunos(lista_alunos)
    
    nome_para_buscar = input("\nDigite o NOME do aluno que deseja excluir: ")

    aluno_para_remover = encontrar_aluno_por_nome(lista_alunos, nome_para_buscar)

    if aluno_para_remover:
        lista_alunos.remove(aluno_para_remover)
        print(f"\nAluno {aluno_para_remover.nome} excluído com sucesso!")
    else:
        print(f"\nAluno com nome '{nome_para_buscar}' não encontrado.")

# Loop principal do Menu
while True:
    print("""
=== Sistema de Gestão Acadêmica ===
1 - Adicionar Aluno
2 - Mostrar Todos
3 - Atualizar Dados
4 - Excluir Aluno
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
            adicionar_aluno(lista_alunos)
        case 2:
            mostrar_todos_alunos(lista_alunos)
        case 3:
            atualizar_aluno(lista_alunos)
        case 4:
            excluir_aluno(lista_alunos)
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
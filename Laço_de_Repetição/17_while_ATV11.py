import os
os.system("cls")

# Definindo variáveis
menor_salario = 999999999
maior_salario = 0
soma_salario = 0
quantidade_salarios = 0
soma_filhos = 0
quantidade_filhos = 0
quantidade_familia = 0

while True:
    os.system("cls")
    print("""
Código  |  Descrição
   1    |  Adicionar família
   2    |  Sair e exibir resultados
""")
    
    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            # Solicitando dados.
            salario = float(input("Digite seu salário: "))
            filhos = int(input("Números de filhos: "))

            # Total de famílias que responderam a pesquisa
            quantidade_familia += 1

            # Média do salário da população
            soma_salario += salario
            quantidade_salarios += 1
            media_salario = soma_salario / quantidade_salarios

            # Média do número de filhos
            soma_filhos += filhos
            quantidade_filhos += 1

            # Maior e Menor salário
            if salario < maior_salario
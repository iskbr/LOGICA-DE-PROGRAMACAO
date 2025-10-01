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
            if salario < menor_salario:
                menor_salario =  salario

            if salario > maior_salario:
                maior_salario = salario

        case 2:
            media_salario = soma_salario / quantidade_salarios if quantidade_salarios != 0 else 0
            
            print("\n= Exibindo resultados =")
            print(f"Total de famílias que responderam a pesquisa: {quantidade_familia}")
            print(f"Média do salário da população: {media_salario}")
            print(f"Média do número de filhos: {quantidade_filhos}")
            print(f"Maior salário: {maior_salario}")
            print(f"Menor salário: {menor_salario}")
        
        case 3:
            print("Saindo do programa.")
            input("Pressione Enter para sair...")
            break
        case _:
            print("Opção inválida, tente novamente.")  
            input("Pressione Enter para sair...")
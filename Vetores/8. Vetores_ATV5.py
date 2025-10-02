import os
os.system("cls")

preco_total = 0
lista_nomes = []
lista_pratos = []

while True:
    print("""
===== MENU =====
Código       Prato            Valor
  1         Picanha         R$ 25,00
  2         Lasanha         R$ 20,00
  3         Strogonoff      R$ 18,00
  4         Bife acebolado  R$ 15,00
  5         Pão com ovo     R$ 5,00        
          """)
   
    opcao = int(input("Digite o código da opção desejada: "))


    match opcao:
        case 1:
            prato = "Picanha"
            preco = 25
        case 2:
            prato = "Lasanha"
            preco = 20
        case 3:
            prato = "Strogonoff"
            preco = 18
        case 4:
            prato = "Bife acebolado"
            preco = 15
        case 5:
            prato = "Pão com ovo"
            preco = 5
        case _:
            print("Opção inválida.")
            print("Tente novamente...")
            preco = 0

    lista_nomes.append(opcao)
    lista_pratos.append(opcao)

    #match lista_nomes:
        #case 1:
            
    preco_total += preco
    
    mais_pedidos = input("Deseja fazer um novo pedido? \nUse S ou N para responder: ").upper()

    os.system("cls")

    if mais_pedidos == "N":
        break


# Mostrando resultado.
print("\n=== RESTAURANTE ===")
print(f"Nome e valor dos pratos: {lista_pratos}")
print(f"Total a pagar: R${preco_total}")

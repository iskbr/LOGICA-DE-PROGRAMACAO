import os
os.system("cls")

valor = float(input("Digite o valor do produto: "))

print("""
\t\t Formas de Pagamento:
1- Pagamento à vista.
2- Pagamento à prazo.

""")

pagamento = int(input("Selecione a forma de pagamento: "))

desconto = (0.1 * valor)
total = (valor - desconto)
2

match pagamento:
    case 1:
        print(f"""
Valor do produto: {valor}
Forma de pagamento à vista.
Valor do desconto: {desconto}
Total a pagar: {total}
""")    
    case 2:
        quantidade_parcelas = int(input("Digite a quantidade de parcelas (1 a 6): "))
       
        if quantidade_parcelas >= 1 and quantidade_parcelas <= 6:
            valor_da_parcela = valor / quantidade_parcelas

            print(f"\nValor do produto: R$ {valor}")
            print("Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {quantidade_parcelas}")
            print(f"Valor por parcela: R$ {valor_da_parcela:.2f}")
            print(f"Total a pagar: R$ {valor}")
        else:
            print("Número de parcelas inválida.")
    case _:
        print("Forma de pagamento inválida.")

print("Volte sempre!")
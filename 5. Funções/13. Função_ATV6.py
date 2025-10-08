import os
os.system("cls")

# Função para transformar em centímetros.
def transformar(n1):
    n1 = n1 * 100
    return n1

# Função para o resultado
def resultado(certo):
    print("==Resultado==")
    print(f"Em centímetros: {certo} cm")

metros = float(input("Digite um valor em metros: ")) # Pedindo o valor
certo = transformar(metros) # Recebe o valor de metros e modifica na função transformar

# Chamando a função resultado.
resultado(certo) # Função para aparecer o resultado pegando a resposta da "certo" e modificando o termo




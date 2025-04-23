import os 

def menu():
    print("\n-- OPÇÕES DE OPERAÇÕES --")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Exponencial")
    print("6 - SAIR")
    
def adicao():
    os.system("cls")  # Limpa a tela 
    lista = []  # Lista para armazenar os valores

    print("Digite os valores para realizar a soma.")
    print("Quando terminar, digite '0' para obter o resultado.")

    # Loop para capturar os valores do usuário
    while True:
        valor = float(input("Digite o valor: "))
        
        if valor == 0:
            break  # Para o loop quando o usuário digitar 0
        
        lista.append(valor)

    # Verificando se a lista contém pelo menos um valor
    if len(lista) == 0:
        print("Erro: é necessário pelo menos um valor para realizar a soma.")
        return

    # Calculando a soma de todos os valores
    resultado = sum(lista)

    # Exibindo o resultado final
    print(f"O resultado da soma é: {resultado}")


def subtracao():
    os.system("cls")  # Limpa a tela 
    lista = []  # Lista para armazenar os valores
    resultado = 0  # Inicia o resultado

    print("Digite os valores para realizar a subtração.")
    print("Quando terminar, digite '0' para obter o resultado.")

    # Loop para capturar os valores do usuário
    while True:
        valor = float(input("Digite o valor: "))
        
        if valor == 0:
            break  # Para o loop quando o usuário digitar 0
        
        lista.append(valor)

    # Verificando se a lista contém valores
    if len(lista) == 0:
        print("Erro: é necessário pelo menos um valor para realizar a subtração.")
        return

    # Realizando a subtração dos valores da lista
    resultado = lista[0]  # Começa com o primeiro valor da lista
    for num in lista[1:]:  # A partir do segundo valor
        resultado -= num  # Subtrai cada número subsequente

    # Exibindo o resultado final
    print(f"O resultado da subtração é: {resultado}")


def multiplicacao():
    os.system("cls")  # Limpa a tela 
    lista = []  # Lista para armazenar os valores
    resultado = 1  # O valor inicial para a multiplicação

    print("Digite os valores para realizar a multiplicação.")
    print("Quando terminar, digite '0' para obter o resultado.")

    # Loop para capturar os valores do usuário
    while True:
        valor = float(input("Digite o valor: "))
        
        if valor == 0:
            break  # Para o loop quando o usuário digitar 0
        
        lista.append(valor)

    # Verificando se a lista contém valores
    if len(lista) == 0:
        print("Erro: é necessário pelo menos um valor para realizar a multiplicação.")
        return

    # Realizando a multiplicação dos valores da lista
    for num in lista:
        resultado *= num  # Multiplica cada número na lista

    # Exibindo o resultado final
    print(f"O resultado da multiplicação é: {resultado}")


def divisao():
    os.system("cls")
    lista = []
    resultado = None

    print("Digite os valores para realizar a divisão.")
    print("Quando terminar, digite '0' para obter o resultado.")

    # Loop para capturar os valores do usuário
    while True:
        valor = float(input("Digite o valor: "))
        
        if valor == 0:
            break  # Para o loop quando o usuário digitar 0
        
        lista.append(valor)

    # Verificando se a lista tem mais de um valor para realizar a divisão
    if len(lista) < 2:
        print("Erro: é necessário pelo menos dois valores para realizar a divisão.")
        return
    
    # Realizando a divisão sequencial
    resultado = lista[0]  # Começa com o primeiro valor da lista
    for i in range(1, len(lista)):  # A partir do segundo valor
        if lista[i] == 0:
            print("Erro: não é possível dividir por zero.")
            return
        resultado /= lista[i]  # Realiza a divisão sequencial

    # Exibindo o resultado final
    print(f"\nO resultado da divisão é: {resultado}")


def exponencial():
    os.system("cls")
    valor = float(input("Digite o valor: "))  #Captura o valor 
    expoente = float(input("Digite o expoente: ")) #Captura o valor da expoente

    #Realizando a operação
    resultado = valor ** expoente

    #Exibindo o resultado
    print(f"O resultado da operação é: {resultado}")


def sair():
    os.system("cls")
    print("\nFINALIZANDO O PROGRAMA... \n")


def selecao():
    while True:

        menu()

        op=int(input("\nDigite a operação desejada: "))
        if op==1:
            adicao()
        elif op==2:
            subtracao()
        elif op==3:
            multiplicacao()
        elif op==4: 
            divisao()
        elif op==5: 
            exponencial()
        elif op==6:
            sair()
            break
        else:
            os.system("cls")
            print("\nOPÇÃO INEXISTENTE \n DIGITE OUTRO VALOR ENTRE AS OPÇÕES")

if __name__=="__main__":

    selecao()

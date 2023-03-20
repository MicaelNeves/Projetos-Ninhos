def mult(numero,numero2):
    resultado = numero * numero2
    return f"Resultado da multiplicação = {resultado}"
    
def soma(numero,numero2):
    resultado = numero + numero2
    return f"Resultado da soma = {resultado}"
    
def subtracao(numero,numero2):
    resultado = numero - numero2
    return f"Resultado da subtração = {resultado}"

def divisao(numero,numero2):
    if numero2==0:
        print("Erro na divisão por zero")
    else:
        resultado = numero/numero2
        return f"Resultado da divisão = {resultado:,.2f}"


while True:
    print(f'''
    soma  - 1
    multiplicação - 2
    subtração - 3
    divisão - 4
    sair - 0
    ''')

    numero = float(input("Digite um numero: "))
    numero2 = float(input("Digite um outro numero: "))
    operador = input("Qual a operação escolhida ou aperte zero para sair: ")
    
    if operador == '1':
        print(soma(numero,numero2))
    elif operador == '3':
        print(subtracao(numero,numero2))
    elif operador == '2':
        print(mult(numero,numero2))
    elif operador == '4':
        print(divisao(numero,numero2))
    elif operador == '0':
        break
    elif not operador.isnumeric():
        print("Valor Invalido")
    else:
        print("Erro")



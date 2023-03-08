def mult(numero,numero2):
    resultado = numero * numero2
    return f"Resultado da Multiplicação = {resultado}"
    
def soma(numero,numero2):
    resultado = numero + numero2
    return f"Resultado da Soma = {resultado}"
    
def subtracao(numero,numero2):
    resultado = numero - numero2
    return f"Resultado da Subtração = {resultado}"
def divisao(numero,numero2):
    if numero2==0:
        print("Erro na divisão por zero")
    else:
        resultado = numero/numero2
        return f"Resultado da Divisão = {resultado:,.2f}"


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
    
    match operador:
        case '1':
            print(soma(numero,numero2))
        case '3':
            print(subtracao(numero,numero2))
        case '2':
            print(mult(numero,numero2))
        case '4':
            print(divisao(numero,numero2))
        case '0':
            break

    if not operador.isnumeric():
        print("Valor Invalido")

# Receba um numero inteiro e, a a partir de funções, imprima a tubuada desse numero de acordo com  vontade do operador
# O operador poderá escolher a tubuada da soma, subtração, divisão, multiplicação ou todas
# Inclua um metodo para que não seja quebrado o programado e adicione uma opção de saída para o operador
# OBS: Cuidado com a tabuada da divisão, adicione somente duas casas decimais

# EX: num = 13
#      SOMA             SUBTRAÇÃO          MULTIPLICAÇÃO        DIVISÃO
#   13 + 0 = 13         13 - 0 = 13          13 X 0 = 0        13 / 0 = 0
#   13 + 1 = 14         13 - 1 = 12          13 X 1 = 13       13 / 1 = 13
#   13 + 2 = 15         13 - 2 = 11          13 X 2 = 26       13 / 2 = 6,25
# .
# .
# .
#   13 + 10 = 23        13 - 10 = 3           13X10 = 130      13 / 10 = 1,30

i = 1
a = 1
b = 1
c = 1
d = 1
def mult(num):
    for i in range(1,11):
        print(f"{num}+{i} = {num+i} ")

def subtracao(num):
    for a in range(1,11):  
        print(f"{num}-{a} = {num-a} ")

def soma(num):
    for b in range(1,11):
        print(f"{num}+{b} = {num+b} ")

def divisao(num):
    for c in range(1,11):
        print(f"{num}\{c} = {num/c:,.2f} ")

def todas(num):
    for d in range(1,11):
        print("  SOMA          SUBTRAÇÃO            MULTIPLICAÇÃO           DIVISÃO  ")
        for d in range(1,11):
            print(f'''{num}+{d} = {num+d}        {num}-{d} = {num-d}         {num}x{d} = {num*d}        {num}\{d} = {num/d:,.2f} 
                ''')





while True:

    print("==============================")
    print(f''' 
    OPERACOES     CODIGO
    SOMA            1
    MULTIPLICACAO   2
    SUBTRACAO       3
    DIVISAO         4
    TODAS           5
    SAIR            0''')
    print("==============================")

   

    a = input("Digite um numero: ")

    operador = input("Escolha a operação ou aperte zero para sair: ")
    try:
        num = int(a)
        
        match operador:
            case '1':
                print(soma(num))
            case '3':
                print(subtracao(num))
            case '2':
                print(mult(num))
            case '4':
                print(divisao(num))
            case '5':
                print(todas(num))
            case '0':
                break

    except:
        print("Erro para os valores ou operação")






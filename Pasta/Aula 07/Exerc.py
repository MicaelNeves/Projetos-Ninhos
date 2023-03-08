# Exemplo 01

def sequencia(numero):
    for i in range(numero):
        i += 1 
        print( str(i)*i)

    for i in range(1,numero+1): 
        cont = 1
        while True:
            print(i,end=' ')
            if cont == i:
                break
            cont += 1
        print()

#numero = int(input("Digite um numero qualquer: "))
#sequencia_4(numero)

# Exemplo 02

def sequencia_1(numero):
    for i in range(1, numero):
        contador = 1
        while contador<= numero:
            aux = 1
            texto = ''
            while aux <= contador:
                texto = texto + str(aux) + "\t" 
                aux += 1
            contador += 1
            print(texto)

#numero = int(input("Digite um numero qualquer: "))
#sequencia_4(numero)  
            
# Exemplo 03

def sequencia_3(a,b,c):
    soma = a + b + c
    return soma

a = int(input("Digite um numero qualquer: "))
b = int(input("Digite um numero qualquer: "))
c = int(input("Digite um numero qualquer: "))
print(f"soma = ",sequencia_3(a,b,c))

# Exemplo 04

def sequencia_4(numero):
    if numero >0:
        char = 'P'  
        print(char)
    else:
        char = 'N'
        print(char)

#numero = int(input("Digite um numero qualquer: "))
#sequencia_4(numero)

# Exemplo 05

def sequencia_5(venda, taxaImposto):
    custo_venda = (taxaImposto/100)*venda + venda
    return custo_venda

taxaImposto = float(input("Digite o valor da taxa imposto: "))
venda = float(input("Digite o valor da venda/ custo de um item: "))
print("Custo Final: ",sequencia_5(venda,taxaImposto))

# Exemplo 06

def sequencia_6(a,b):
    if a<=12:
        print(f"{a} : {b}")
    elif a>12 and a <=23: 
        for i in range(1,a):
            i+=1
        print(f"{i}: {b}")
    else: 
        print("erro")


def sequencia_6_1(i):
    if i == 'A':
        print("A.M")
    elif i == 'P':
        print("P.M")

while True: 
    a = int(input("Digite as horas: "))
    b = int(input("Digite os minutos: "))
    c = str(input("Digite A para A.M ou P para P.M: "))

    sequencia_6(a,b), sequencia_6_1(c)

    aux = input("Deseja continuar SIM/NAO:")

    if aux=='SIM':
        pass
    else:
        break

# Exemplo 07


def valorPagamento(valor, dias_atraso):
    if dias_atraso == 0:
        return valor
    elif dias_atraso != 0 and dias_atraso > 0:
        return valor + (valor)*0.03 + (valor)*(0.01)*(dias_atraso)
    else:
        return print("Erro na execução do programa")


while True:

    valor = float(input("Digite o valor da prestação: "))
    dias_atraso = int(input("Digite a quantidade de dias em atraso: "))
    print(f"O valor a ser pago é de R$ {valorPagamento(valor,dias_atraso):,.2f}")

    if valor != 0:
        pass
    elif not valor.isnumeric():
        print("Digite um valor de prestação numerico")
    elif valor < 0:
        print("Digite um valor de prestação positivo")
    else:
        break


# Exemplo 08

def sequencia_8(valor):
    for i in range(1,len(valor)):
        i += 1
    return i 
a = input("Digite um numero qualquer: ")
print(sequencia_8(a))

# Exemplo 09

import os
os.system('cls')


def reverso(valor):
    valor1 = str(valor)[::-1]
    return valor1


while True:
    try:
        valor = int(input("Digite um valor inteiro: "))
    except:
        print("Digite um numero natural")
    else:
        print(f"O reverso é {reverso(valor)}")
        break
     
# Exemplo 10

import random

def jogar_dados():
    dado_1 = random.randint(1, 6)
    dado_2 = random.randint(1, 6)
    print(f'Primeiro dado: {dado_1}')
    print(f'Segundo dado: {dado_2}')
    return dado_1 + dado_2

rodada = 1
ponto = 0
validador = False
while True:
    iniciar = input('Desejar lançar um par de dados? [S]Sim [N]não: ')
    iniciar = iniciar.upper()
    if iniciar == 'S':
        soma = jogar_dados()
        if rodada == 1:
            if soma == 7 or soma == 11:
                print('Você é um "natural" e ganhou')
                break
            elif soma == 2 or soma == 3 or soma == 12:
                print('Craps - Você Perdeu')
                break
            elif soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10:
                print(f'{soma} este é seu ponto')
                ponto = soma
                print('Seu objetivo agora é continuar jogando os dados até tirar este número novamente.')
            rodada += 1
        else:
            if ponto == soma:
                validador = True
                print('Tirou o seu ponto')
                print('Agora já pode tirar 7 pra ganhar')
                rodada += 1
            elif (validador == False) and soma == 7:
                print('Você perdeu')
                rodada += 1
                break
            elif (validador == True) and soma == 7:
                print('Você ganhou')
            else:
                 print('Seu objetivo agora é continuar jogando')

    else:
        break

# Exemplo 11

def  sequencia_11(d,m,a):
    
    if m=='01' or m =='1':
        print(f"{d}/{m}/{a}")
        m = 'Janeiro'
        print(f"{d} de {m} de {a}")
    elif m=='02' or m =='2':
        print(f"{d}/{m}/{a}")
        m = 'Fevereiro'
        print(f"{d} de {m} de {a}")
    elif m=='03' or m =='3':
        print(f"{d}/{m}/{a}")
        m = 'Março'
        print(f"{d} de {m} de {a}")
    elif m=='04' or m =='4':
        print(f"{d}/{m}/{a}")
        m = 'Abril'
        print(f"{d} de {m} de {a}")
    elif m=='05' or m =='5':
        print(f"{d}/{m}/{a}")
        m = 'Maio'
        print(f"{d} de {m} de {a}")
    elif m=='06' or m =='6':
        print(f"{d}/{m}/{a}")
        m = 'Junho'
        print(f"{d} de {m} de {a}")
    elif m=='07' or m =='7':
        print(f"{d}/{m}/{a}")
        m = 'Julho'
        print(f"{d} de {m} de {a}") 
    elif m=='08' or m =='8':
        print(f"{d}/{m}/{a}")
        m = 'Agosto'
        print(f"{d} de {m} de {a}")
    elif m=='09' or m =='9':
        print(f"{d}/{m}/{a}")
        m = 'Setembro'
        print(f"{d} de {m} de {a}")
    elif m=='10':
        print(f"{d}/{m}/{a}")
        m = 'Outubro'
        print(f"{d} de {m} de {a}")
    elif m=='11':
        print(f"{d}/{m}/{a}")
        m = 'Novembro'
        print(f"{d} de {m} de {a}")
    elif m=='12':
        print(f"{d}/{m}/{a}")
        m = 'Dezembro'
        print(f"{d} de {m} de {a}")   
    else:
        print("Erro")

d = input("Dia: ")
m = str(input("Mes: "))
a = input("Ano: ")
# lista = data.split("/")
print(sequencia_11(d,m,a))




















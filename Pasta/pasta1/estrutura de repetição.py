#Exemplo 01

print("==============================")
aux2 = print(f''' 
OPERACOES     CODIGO
SOMA            1
SUBTRAÇÃO       2
MULTIPLICACAO   3
DIVISAO         4
TODAS            1
SAIR            0''')
print("==============================")

num = 13
while True:
    i = 1
    a = 1
    b = 1
    c = 1
    d = 1
    cod = int(input("Digite a tabuada: "))
    if  cod == 1 or cod == 2 or cod == 3 or cod == 4 or cod==5:
        if cod == 1:
            for i in range(1,11):
                print(f"{num}+{i} = {num+i} ")
        elif cod == 2:
            for a in range(1,11):  
                print(f"{num}-{i} = {num-i} ")
        elif cod == 3:
            for b in range(1,11):
                print(f"{num}x{b} = {num*b} ")
        elif cod == 4:
            for c in range(1,11):
                print(f"{num}\{c} = {num/c:,.2f} ")
        elif cod == 5:
            print("  SOMA          SUBTRAÇÃO            MULTIPLICAÇÃO           DIVISÃO  ")
            for d in range(1,11):
                print(f'''{num}+{d} = {num+d}        {num}-{d} = {num-d}         {num}x{d} = {num*d}        {num}\{d} = {num/d:,.2f} 
                ''')
    elif cod == 0:
        print("Encerrou o programa")
        break
    else:
        print("Erro")



#Exemplo 02
'''

aux = 0
for i in range(10):
    numero = int(input("Digite um numero: "))
    if numero >= 10 and numero <=50:
        aux = aux + 1
print(aux)

'''

# Exemplo 04
'''
soma = 0
i = 1
for i in range(101):
    soma = soma + i
print(soma)

'''
# Exemplo 06

num  = int(input("Digite um numero: "))
i = 1
a = 0
for i  in range(1,num):
    rest = num / i
    if rest%0:
        a += 1
        print(a)
        



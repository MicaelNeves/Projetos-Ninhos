'''
def hello(nome):
    print("Hello", nome)
'''
#nome = input("What's your name: ")
#hello(nome)
'''
def calcPag(horas, valhora):
    horas = float(horas)
    taxa = float(valhora)
    if horas <= 40:
        salario = horas*taxa
    else:
        excd =horas - 40
        salario = 40*taxa + (excd*(1.5*taxa))
    return salario

h = int(input("Digite a quantidade de horas: "))
v = int(input("Digite o valor pago por horas: "))
total = calcPag(h,v)
print(f"Salario igual a R$ {total}")
'''
'''
def calc_imc(peso, altura):
    print(peso/altura**2)

print(f"{calc_imc(peso = 47, altura = 1.55)}")

'''

def e(b):
    a = b*b
    return a

a = 10
e(a)
e(a)
print(e(a))




def myname():
    import random

    nome = str(input("Digite seu nome: "))
    nome_novo = nome.random()
    print(nome_novo)
'''
def reverso(valor):
    return str(valor)[::-1]

valor = int(input("Digite um numero: "))
print(f"Valor Reverso: {reverso(valor)}")
'''
'''
def quantidade(valor):
    aux = 0
    valor = str(valor)
    for i in range(len(valor)):
        aux += 1
    return aux
    

n = input("Digite um numero: ")
print(f"Valor: {quantidade(n)}")
'''
def digitos(n):
    return len(str(n))

print(digitos(123200000222))

def potencia(base,expoente):
    resultado = 1
    for numero in range(1,expoente+1):
# base ** expoente = base * base (expoente vezes)
        resultado = resultado * base
    return resultado

print(potencia(2,3))

def f4(a):
    global c
    print(c)
    c = 10
    print(c)
    print(a+x+c)

x = 4
c = -1
f4(1)
print(c)
def f5(a):
    a.append(3)
a = [1,2]
f5(a)
print(a)
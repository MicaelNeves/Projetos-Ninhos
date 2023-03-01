'''
pessoa = {"Nome":'Micael',"idade":'21', "Nacionalidade": 'Brasileira'}

print(pessoa["Nome"]) # retorna o valor da chave

print(pessoa) # Retorna os valores do dicionario 

print(pessoa.keys())   # retorna o valor das chaves 
print(pessoa.values())  # retorna os valores das chaves
print(pessoa.items())   # retorna tanto os valores com a chave 

pessoa["Estado"] = 'CE'  #acrescenta ou muda uma chave 

print(pessoa)

print(pessoa.get("Nome"))  # verifica se existe a chave e retorna o valor da chave

pessoa2 = pessoa.copy() # faz uma copia do dicionario
del pessoa2["Nacionalidade"] # Exclui uma chave do dicionario
print(pessoa)
print(pessoa2)
'''
# Exemplo 01
'''
pessoa = {"Nome": 'Micael', "Ultimo nome": 'Neves',"idade":'21',"Curso": 'Programador',"Endereco":'Avenida'}

print(pessoa)

print(pessoa["Nome"])
print(pessoa["Ultimo nome"])
print(pessoa["idade"])
print(pessoa["Curso"])
print(pessoa["Endereco"])

pessoa["Ultimo nome"] = 'Lopes'
print(pessoa)

print(pessoa["Endereco"])

pessoa2 = pessoa.copy()

pessoa2["Nome"] = 'Mikaelz'
pessoa2["idade"] = '24'

print(pessoa2)
'''
# Exemplo 02

# manipulação do laço de incremento
'''
lista = range(100,200,2)
print(list(lista))

hello = "Hello World"
novoHello = list(hello)
novoHello[0] = "J"
print(novoHello)

print(''.join(novoHello))
'''
# Operadores logicos
#'''
'''
while True:
    num = int(input("digite um numero inteiro; "))
    if (num > 10 and num < 20):
        print("Está no intervalo")
    else:
        print("Não está no intervalo")
    if num==0:
        break
'''
'''
idade  = int(input("Digite sua idade: "))

if idade>= 10 and idade<20:
    print("Você é um adoslecente")
elif idade >= 20 and idade < 30:
    print("Você é jovem")
elif idade>=30 and idade<=100:
    print("Você é um adulto")
else:
    print("INIMIGO DO INSS")
'''
# EXERCICIOS

# Exemplo 01
'''
a = int(input("Digite um número A: "))
b = int(input("Digite um número B: "))
c = int(input("Digite um número C: "))

if a+b<c:
    print(f"{a} + {b} é menor  que {c}")
else:
    print(f" A soma não é igual a {c}")
'''
# Exemplo 02
'''
num = int(input("Digite um número: "))

if num%2 == 0:
    print(f"O numero {num} é par")
else:
    print(f"O numero {num} é ímpar")
'''
# Exemplo 03
'''
a = int(input("Digite um número A: "))
b = int(input("Digite um número B: "))

if a==b:
    soma = a + b
    print(f"Soma= {soma}")
else:
    mult = a*b
    print(f"Multiplicação = {mult}")
'''

# Exemplo 04
'''
a = int(input("Digite um número A: "))
b = int(input("Digite um número B: "))
c = int(input("Digite um número C: "))

if a==b or b==c or a==c:
    print("Valores são iguais e precisam ser diferentes")
elif a>b and a>c and b>c:
    print(a,b,c)
elif a>b and a>c and b>c:
    print(a,c,b)
elif b>a and b>c and a>c:
    print(b,a,c)
elif b>a and b>c and a<c:
    print(b,c,a)
elif c>a and c>b and b>a:
    print(c,b,a)
elif c>a and c>b and b<a:
    print(c,a,b)
else:
    print("Erro")

'''
# Exemplo 05

nome = input("Digite seu nome: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:  "))
nota3 = float(input("Digite a terceira nota:  "))

media = (nota1 + nota2 + nota3)/3

if media>=7.0:
    print(f''' 
    ========================
    Nome - {nome.upper()}
    Situação - Aprovado
    ========================''')
elif media <= 5:
    print(f''' 
    ========================
    Nome - {nome.upper()}
    Situação - Reprovado
    ========================''')
elif media<=5.1 and media<=6.9:
    print(f''' 
    ========================
    Nome - {nome.upper()}
    Situação - Recuperação
    ========================''')
else:
    print("Erro na Nota")

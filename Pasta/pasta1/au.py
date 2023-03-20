'''
# Equipe 01: 

Elabore o jogo pedra, papel e tesoura.


requisitos:
1 - criar menu inicial
2 - que seja um jogador contra a máquina
3 - os movimentos do oponente devem ser escolhidos aleatoriamnete(Dica: biblioteca random)
4 - com o resultado da partida( "voce venceu", "voce perdeu" e "empate"
'''


#Equipe 2:

# faça um programa que escolha um número aleatório entre 1 e 100, 
# e peça para o usuário inserir um valor como palpite.
#  O programa deve continuar até acertar e deve informar se está maior ou menor que o valor sorteado.
# ( Faça o programa ler intervalos entre dois números)

from random import randint
def numero_aleatorio():
    aleatorio = randint(1,100)
    palpite = 0
    while aleatorio != palpite:
        palpite = int(input("Digite um valor( 1 a 100):"))
        if (aleatorio == palpite):
            print("Parabens, Você Acertou!")
        else:
            palpite = int(palpite)
            if aleatorio > palpite:
                print("O valor é maior")
                print("Tente Novamente")
            elif aleatorio < palpite:
                print("O valor é menor")
                print("Tente Novamente")
numero_aleatorio()






#Equipe 3:

# Escreva um programa q contenha uma função que  imprima os numeros de 0 a um numero escolhido. 
#Para multiplos de 3 imprima "Ninho" na frente do numero 
#e para os multiplos de cinco imprima " para os multiplos de cinco imprima "desenvolvedor". ". 
#Para números que sao multiplos de tres e cinco imprima "Nindo de Desenvolvedores"
#para o restante dos números imprima Senac
'''
def valor(num):
    i = 0
    aux = int(num)
    while i <= aux:
        print(i)
        i += 1
    if aux == 3:
        print(f"Ninho - {aux}")
    if aux%5 == 0:
        print(f"Desenvolvedor")
    if (aux%5== 0 and aux%3==0):
        print("Nindo de Desenvolvedores")
    else:
        print("Senac")
    

num = input("Digite um numero: ")
print(valor(num))
if num == 3:
    print(f"Ninho - {num}")
elif num%5== 0:
    print(f"Desenvolvedor")
elif num%5 == 0 and num%3==0:
    print("Nindo de Desenvolvedores")
else:
    print("Senac")

'''
#Equipe 4:

# Crie um algoritmo que receba 3 valores referentes aos lados de um triangulo e informe se os valores formam 
# realmente um triagulo ou não.
# Caso os valores formem um triangulo o algoritmo deve informar que tipo de triangulo foi formado 
# (Equilátero, Isósceles ou Escaleno).

a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))
    
# Testando se é triângulo
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Nao é um triangulo')
elif (a == b) and (a == c) :
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isósceles')
else:
    print('Escaleno')

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



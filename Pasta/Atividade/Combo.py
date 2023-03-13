# Lista 01
-
#Escreva uma função que receba como parâmetro uma lista de números inteiros e retorne a soma dos números pares na lista. 
#Em seguida, utilize um laço de repetição para solicitar ao usuário uma lista de números inteiros, chame a função e imprima o resultado.


'''

def questao01(lista):
    sum = 0
    n = 1
    lista_nova = []
    for i in range(len(lista)):
        if lista[i]%2==0:
            sum = sum + lista[i]
    print(f"A soma dos numeros paresm da lista é {sum}")
    quant = int(input("Digite a quantidade de elementos de sua nova lista: "))
    while n<=quant:

        try: 
           lista_nova.append(int(input("Digite um numero inteiro: ")))
        except:
            ("Erro no código")
        n += 1
    print(lista_nova)

lista = [1,2,3,4,5,6,7,8,9,10]
print(questao01(lista))

'''

# Questão 03

#Escreva uma função que receba como parâmetro uma lista de strings e retorne a quantidade de strings que possuem mais de 5 caracteres. 
#Em seguida, utilize uma estrutura condicional para perguntar ao usuário se ele deseja adicionar mais strings à lista,
#e utilize um laço de repetição para solicitar ao usuário as novas strings, chame a função e imprima o resultado.

'''
def questao03(lista):
    aux = 'sim'
    count = 0 
    for i in range(len(lista)):
        if len(lista[i])>5:
               print(lista[i])
               count += 1
    print(f"A quantidade de string com mais de 5 caracteres na lista: {count}")

    while aux == 'sim':
        aux = input("Você deseja adicionar mais strings na listas? [sim] [nao] : ")
        
        if aux == 'sim':
            lista.append(input("Digite a nova string: "))
            print(lista)
        else:
                break
    

lista = ['Micael', 'aaa','ninho','programa']
print(lista)
print(questao03(lista))
'''


# Questão 04

#Escreva uma função que receba como parâmetro uma lista de números inteiros e retorne o número máximo na lista.
#Em seguida, utilize uma estrutura de repetição para solicitar ao usuário uma lista de números inteiros, chame a função e imprima o resultado.
#Se a lista estiver vazia, a função deve retornar None e o programa deve imprimir uma mensagem informando que a lista está vazia.


def questao04(lista):
    maximo = 0
    lista_nova = []
    n = 1 
    for i in range(len(lista)):
        if maximo <= lista[i]:
            maximo = lista [i]
    print(f"O numero maximo da lista: {maximo}")
    quant = int(input("Digite a quantidade de elementos de sua nova lista: "))
    while n<=quant:
        try: 
           lista_nova.append(int(input("Digite um numero inteiro: ")))
        except:
            ("Erro no código")
        n += 1
    print(lista_nova)
    if lista_nova == []:
        print("a lista está vazia")
        return None
    
    


lista = [100,2,3,4,5,6,7,8,9,10,45]
print(questao04(lista))

# Questão 05

#Escreva uma função que receba como parâmetro um número inteiro n e retorne uma lista com os n primeiros números da sequência de Fibonacci.
#Em seguida, utilize uma estrutura condicional para perguntar ao usuário se ele deseja gerar a sequência de Fibonacci para outro número,
#e utilize um laço de repetição para solicitar ao usuário os novos valores de n, chame a função e imprima o resultado.



'''
def questao05(n):
    lista = [1,1]
    geral = 1
    geral2 = 1
    aux = 0
    if n>=2: 
        for i in range(0,n-2):
            aux = geral + geral2
            geral = aux
            geral2 = aux - geral2
            lista.append(aux) 
        return print(lista)
    elif n ==1:
        return print(lista[0])
    else:
        return print("Digite um numero natural maior que zero")



n = int(input("Digite o n-esimo termo da sequencia: "))
print(questao05(n))
while True:     
        ordem = input("Você deseja continuar? [sim] [nao] : ")
        if ordem == 'sim':
            n = int(input("Digite o n-esimo termo da sequencia: "))
            print(questao05(n))
        else:
            break
'''
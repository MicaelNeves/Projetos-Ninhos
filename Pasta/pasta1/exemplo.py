'''
def string_length(str1):
    count = 0
    for char in str1:
        count += 1
    return count
print(string_length('w3resource.com'))
'''
'''
str('Micael')
count = 0
for char in str:
    count+=1 
print(count)'''
'''
# Escreva um programa Python para calcular o comprimento de uma string.
sum_list = 0  
list = [1,2,-8]
for x in list:  
    sum_list += x  
print(sum_list) 

#  Escreva um programa em Python para somar todos os itens de uma lista
lista = [2,10,8]
multi = 1
for mult in lista:
    multi = multi * mult
print(multi)

#Escreva um programa em Python para obter o maior número de uma lista
lista1 = [2,3,4]
maior = 0 
aux = 0
for aux in lista1:
    if aux > maior:
        maior = aux
print(aux)
'''
'''
#Escreva um programa em Python para obter o menor número de uma lista

list = [ 1,2,3,0,4]
min = 0 
for a in list:  
    if a < min:  
        min = a 
print(min)
'''

'''
lista = []
lista1 = []
for i in range(5):   
    lista.append(int(input("Digite um numero: ")))
    numero = int(input("Numero= "))
    lista1.append(numero)
print(lista)
print(lista1)
'''
'''
lista = ['abc', 'xyz', 'aba', '1221']
count = 0 
for i in lista:
    if  lista[0] == lista[-1]:
        count+=1
print(count)'''
'''
vogais = ('a','e','i','o','u')
print(type(vogais))
print(len(vogais))
'''
'''
lista = ['m','i','c','a','e','l']
print(lista[0])
print(len(lista))
'''
'''
lista = "Micael"
aux = lista[::-1]
print(aux)
'''   
# Exemplo 01
nome = input("Nome: ")
numero_qtd = len(nome) - nome.count(" ")
contador = 0 
print(f" Primeira letra: ",nome[0])
print(f"Quantidade: ",numero_qtd)

# Exemplo 02
nome = input("Nome: ")
print(nome[::-1])

# Exemplo  03

palavra = "Micael"
inverso = ""

for i in range(len(palavra)):
    inverso += palavra[(len(palavra)-i-1)]
print(inverso)
'''
lista = ["micael"]
lista_aux = []
for i in len(lista):
    if i%2!=0:
        lista_aux += lista[i]
'''

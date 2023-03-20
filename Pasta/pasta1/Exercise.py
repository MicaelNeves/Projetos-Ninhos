
# 1 - Write a Python program to clone or copy a list
def questao01():
    lista = [1,4,3,5,6]
    lista_copy = lista.copy()
    print(lista_copy)

# 2 - Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
def questao02():
    palavra = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print(palavra)
    del palavra [0]
    del palavra [3]
    del palavra [3]
    print(palavra)

# 3 - Escreva um programa em Python para obter o menor número de uma lista
def questao03():
    list = [ 1,2,3,0,4]
    min = 0 
    for a in list:  
        if a < min:  
         min = a 
    print(min)

# 4 -  Write a Python program to add an item to a tuple
def questao04():
    tupl = (1,2,3)
    tupl += (9,)
    print(tupl)

# 5 - Write a Python script to add a key to a dictionary.
def questao05():
    dicionario = {0: 10 , 1: 20}
    dicionario.update({2:30})
    print(dicionario)

# 6 - Write a Python program to sum all the items in a dictionary.
def questao06():
    typ = {'mica':22, 'john': 13,'froz':19}
    print(sum(typ.values()))

# 7 - Escreva um programa em Python para obter o maior número de uma lista
def questao07():
    lista1 = [2,3,4]
    maior = 0 
    aux = 0
    for aux in lista1:
       if aux > maior:
           maior = aux
    print(aux)

# 8 - Escreva um programa Python para calcular o comprimento de uma string.
def questao08():
    sum_list = 0  
    list = [1,2,-8]
    for x in list:  
      sum_list += x  
    print(sum_list) 

# 9 - Escreva um programa em Python para somar todos os itens de uma lista
def questao09(): 
    lista = [2,10,8]
    multi = 1
    for mult in lista:
     multi = multi * mult
    print(multi)

# 10 - Write a Python program to remove duplicates from a list.
def questao10():
    lista = [1,2,3,4,5,6,7,8,6,7,1]
    dupl = set()
    aux = []
    for i  in lista:
     if i not in dupl:
          aux.append(i)
          dupl.add(i)
    print(dupl)

print("Nome: Micael dos Santos das Neves")
print(f'''
RESOLUÇÃO 
1 - QUESTÃO 
2 - QUESTÃO 
3 - QUESTÃO 
4 - QUESTÃO 
5 - QUESTÃO 
6 - QUESTÃO 
7 - QUESTÃO 
8 - QUESTÃO 
9 - QUESTÃO 
10 - QUESTÃO 
''')
aux = int(input("Digite o numero da questão: "))
if aux==1:
   questao01()
elif aux==2:
   questao02()
elif aux==3:
   questao03()
elif aux==4:
   questao04()
elif aux==5:
   questao05()
elif aux==6:
   questao06()
elif aux==7:
   questao07()
elif aux==8:
   questao08()
elif aux==9:
   questao09()
elif aux==10:
   questao10()
else:
   print('ERROR')


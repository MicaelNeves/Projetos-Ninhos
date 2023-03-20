
def  questao06():
    lista = [(2,5),(1,2),(4,4),(2,3),(2,1)]
    listaNova = []
    for tuple in lista:
        listaNova.append(tuple[::-1])
    listaNova.sort()
    lista.clear()
    for tuple in listaNova:
        lista.append(tuple[::-1])
    print(lista)

#questao06()

def questao061():
    lista = [(2,5),(1,2),(4,4),(2,3),(2,1)]
    listaNova = []
    menor = None
    for x in range(len(lista)):
        for tupla in lista:
            if ((menor == None or tupla[1]<menor[1]) and tupla not in listaNova):
                menor = tupla
        if( menor not in listaNova):
            listaNova.append(menor)
        menor = None

    print(listaNova)

# questao061()



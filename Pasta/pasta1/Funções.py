
# Exemplo 01
'''
def conta(valor):
    gorjeta = valor*0.10
    print(f"Gorjeta do Funcionario: R$ {gorjeta:,.2f}")
    return gorjeta

print("=====RESTAURANTE MARES=====")
valor = int(input("Qual o valor da Conta do Cliente: R$ "))
conta(valor)
'''
# Exemplo 02 
'''
def letra(palavra):
    aux = 0
    for i in range(len(palavra)):
        if 'a' == palavra[i]:
         aux += 1
    return aux

palavra = str(input("Digite um nome: "))
a = letra(palavra)
print(f"Quantas letras (a) apareceram : {a}")
'''
# Exemplo 03

def limite(S, Inf, lista):
    novaLista = []
    for i in lista:       
        if Inf <= i <= S:
            novaLista.append(i)
    return novaLista

lista = [12,14,15,16,18,20,24,26,28,32,34,38]
limSup = int(input("Digite o limite superior: "))
limInf = int(input("Digite o limite inferior: "))
limite(limSup, limInf, lista)
print(limite(limSup, limInf, lista))

    
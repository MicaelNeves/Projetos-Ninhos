
def questao():
    num1 = int(input("Escreva um numero: "))
    num2 = int(input("Escreva um numero: "))
    num3 = int(input("Escreva um numero: "))

    lista = [num1, num2, num3]
    lista.sort(reverse = True)
    print(lista)

while True:

    questao()
    print("================")
    aux = str(input("Você pretende continuar: "))
   
    if aux == 'sim' or aux == 's' or aux =='S' or aux == 'SIM':
        pass
    else: 
        break
    





while True:
    print("===================================")
    numero = int(input("Digite um numero inteiro: "))

    if numero < 12:
        print("Numero menor que 12")
    elif numero==12:
        print("Numero igual a 12")
    elif numero ==20:
        print("Numero igual a 20")
    elif numero >= 12 and numero < 20:
        print("Numero menor que 20")
    else:
        print("Numero maior que 20")

    print("===================================")
    aux = str(input("Você pretende continuar: "))
    
    if aux == 'sim' or aux == 's' or aux =='S' or aux == 'SIM':
        pass
    else: 
        break


# Tipos de Dados

'''
def questao01(num):
    valor = 2*num
    return valor

num = int(input("Digite um numero inteiro: "))
print(f"O dobro desse numero é {questao01(num)}")

def questao02(raio):
    pi = 3.14
    area = pi*(raio**2)
    return area

raio = float(input("Digite o raio do circulo: "))
print(f"A área do circulo é igual a {questao02(raio):.2f}")


def questao03(nome,idade):
    print("Olá", nome)
    print(f"Feliz",idade, "anos!")
    

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print(questao03(nome, idade))

'''
# Coleções


def a(nome):
    nome = str(nome)
    i = 0 
    for i in range(len(nome)):
        if nome[i] == nome[i][::-1]:
            aux = print(f"{nome} é um palindromo")
        else:
            aux = print(f"{nome} não é um palindromo")
    return aux



nome =input("Digite uma palavra: ")
print(a(nome))




# EXEMPLO 06

num  = int(input("Digite um numero: "))
i = 1
a = 0
for i  in range(2,num):
    if num%i==0:
        a = a+1
if a == 0:
    print(f"{num} é primo")
else:
    print(f"Tem {a} divisores e, portanto, NÃO É PRIMO")

# EXEMPLO 05

largura = int(input("Digite um numero: "))
altura = int(input("Digite um numero: "))
linha = ''

for i in range(largura):
    linha = linha + '#'
retangulo = ''
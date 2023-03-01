
# Dado o nome de uma pessoa, retorne o número de letras do nome e a primeira

nome = input("Digite seu nome: ")
listaNome1 = len(nome) - nome.count(" ")
print(f"A quantidade de letras é igual a {listaNome1}")
print(f"A letra inicial é {nome[0]}")

# Dada uma palavra, retorna a palavra invertida

nome = input("Digite seu nome: ")
print(nome[::-1])

palavra = "Micael"
inverso = ""

for i in range(len(palavra)):
    inverso += palavra[len(palavra)-i-1)]
print(inverso)


# Dada uma palavra, retorna os caracteres nas posições impares

palavra = input("Digite uma palavra: ")
i = 0
palavraimp = ''
for i in range(len(palavra)):
    if i%2!=0:
        pass
    else:
        palavraimp += palavra[i]

print(f"Os caracteres nas posições impares: {palavraimp}")
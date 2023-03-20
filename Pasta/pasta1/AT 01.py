
fruta1Nome = input("Nome da fruta 01: ")
fruta2Nome = input("Nome da fruta 02: ")
fruta3Nome = input("Nome da fruta 03: ")
fruta4Nome = input("Nome da fruta 04: ")
fruta5Nome = input("Nome da fruta 05: ")

fruta1Preco = 1.00
fruta2Preco = fruta1Preco*2
fruta3Preco = fruta1Preco/2
fruta4Preco = fruta3Preco*3
fruta5Preco = fruta4Preco/2

print(f''' 
{fruta1Nome.upper()} - R$ {fruta1Preco}
{fruta2Nome.upper()} - R$ {fruta2Preco}
{fruta3Nome.upper()} - R$ {fruta3Preco}
{fruta4Nome.upper()} - R$ {fruta4Preco}
{fruta5Nome.upper()} - R$ {fruta5Preco}
''')
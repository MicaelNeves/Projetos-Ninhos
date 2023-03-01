
pessoa = {"Nome": 'Micael', "Ultimo nome": 'Neves',"idade":'21',"Curso": 'Programador',"Endereco":'Avenida'}

print(pessoa)

print(pessoa["Nome"])
print(pessoa["Ultimo nome"])
print(pessoa["idade"])
print(pessoa["Curso"])
print(pessoa["Endereco"])

del pessoa["Curso"]

pessoa["Ultimo nome"] = 'Lopes'
print(pessoa)

print(pessoa["Endereco"])

pessoa2 = pessoa.copy()

pessoa2["Nome"] = 'Mikaelz'
pessoa2["idade"] = '24'

print(pessoa2)

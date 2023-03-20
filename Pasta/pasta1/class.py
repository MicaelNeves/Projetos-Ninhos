'''
class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self,velocidade):
        print(f"O {self.marca} {self.ano} acelerou {velocidade} km/h")

    def inf(self):
            # print( f"{self.marca} - {self.modelo} - {self.ano}")
            a = f'{self.marca}' '-' f'{self.modelo}' '-' f'{self.ano}'
            return a 

carro = Carro("Fiat","Uno","2000")
carro.acelerar(80)
print(carro.inf())
'''

class Agenda():
    def __init__(self,listContatos,maxContatos):
        self.listContatos = listContatos
        self.maxContatos =maxContatos
    
    def adicionarContato(self):
        while self.maxContatos <= 10:
            self.listaContatos = self.listaContatos.append()
    
    def removerContato(self):
        self.listaContatos = self.listaContatos.pop(self.listContatos)
    
    def inf(self):
         return f'{self.nome} - {self.telefone}'
         
    
class Contato:
    def __init__(self,nome, telefone):
        self.nome = nome
        self.telefone = telefone
    def inf(self):
         return f'{self.nome} - {self.telefone}'


lista1 = Contato("Micaele","12345609")
lista2 = Contato("Micael","123456")
lista3 = Contato("Jose","2342192")

lista1.inf()
#agenda = Agenda(lista1,lista2,lista3)















#https://edisciplinas.usp.br/mod/assign/view.php?id=2423188
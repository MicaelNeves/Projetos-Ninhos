'''
class Pessoa:
    def __init__(self,nome,sexo,cpf):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
    def dizerOla(self):
        print("Olá,",self.nome,"seu cpf é ",self.cpf)

if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "12345")
    print(pessoa1.nome)
    pessoa1.dizerOla()

'''
'''
import random

class Pokemon():
    def __init__(self,nome,tipo, hp,spd,atk,defesa):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.spd = spd
        self.atk = atk
        self.defesa = defesa

        match self.nome:
            case "Charmander":
                self.tip = "Foguinho"
            case "Pikachu":
                self.tip = "Rato Elétrico"
            case _:
                self.tipo = "Normal"
    
    def batalha(self, oponente):
        poder = self.atk + self.defesa + self.hp
        poderOponente = oponente.atk + oponente.defesa + oponente.hp

        if poder>poderOponente: 
            print(f"{self.nome} ganhou com {poder}")
        else:
            print(f"{self.oponente} ganhou com poder {poderOponente}")       
    
        pass


if __name__ == "__main__":

    pokemon1 = Pokemon("Pikachu","Relampago Explosivo","45","60","80","50")
    pokemon2 = Pokemon("Charmander","Fogo","39","50","52","43")
    pokemon3 = Pokemon("Miau","Grama","35","28","45",'37')  
    print(pokemon1.nome,"-",pokemon1.tipo)
    print(pokemon2.nome,"-",pokemon2.tipo)
    print(pokemon3.nome,"-",pokemon3.tipo)
    opcoes = input("Digite o numero do pokemon escolhido: ")

    match opcoes:
        case "1":
            pokemonEscolhido = pokemon1
        case "2":
            pokemonEscolhido = pokemon2
        case "3":
            pokemonEscolhido = pokemon3
        case _:
            print("Digite uma opção válida")
    
    print("você escolheu ",pokemonEscolhido.nome)
    pokemonOponente = random.choice(pokemon1,pokemon2,pokemon3)
    pokemonEscolhido.batalha(pokemonOponente)

'''
'''
class Pessoa:
    def __init__(self,nome,genero,cpf,ativo):
        self.nome = nome
        self.genero =genero
        self.cpf = cpf
        self.ativo =ativo
    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada com sucesso")

pessoa1 = Pessoa("João","M","12345", True)
pessoa1.desativar()
'''
'''
class Triangulo():
    def __init__(self,ladoA,ladoB,ladoC):
        self.ladoA = int(ladoA)
        self.ladoB = int(ladoB)
        self.ladoC = int(ladoC)
    
    def perimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        print("O perimetro é",perimetro)
    
    def getMaiorLado(self):
        maior = 0
        if self.ladoA > self.ladoB and self.ladoA > self.ladoC:
            maior = self.ladoA
        elif self.ladoB > self.ladoA and self.ladoB > self.ladoC:
            maior = self.ladoB 
        elif self.ladoC > self.ladoA and self.ladoC > self.ladoB:
            maior = self.ladoC
        else:
            print("Invalido") 
        print("Lado Maior:",maior)

lado = Triangulo("252","53","472")
lado.perimetro()
lado.getMaiorLado()
'''
'''
class Funcionario:
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def aumentarSalario(self,percentualAumento):
        valor = self.salario + self.salario*(percentualAumento)
        print("O novo salario = ",valor)

a = input("Diga seu salario: ")
harry = Funcionario("Harry", a)

aux = float(input("Digite o percentual de aumento: "))
harry.aumentarSalario(aux)
   
'''

class Livro:
    def __init__(self,nome,paginas,autor,preco):
        self.nome = nome
        self.paginas = paginas
        self.autor = autor
        self.preco = preco

    def getPreco(self):
        print("Preco = ",self.preco)

    def setPreco(self):
        novoValor = float(input("Digite o novo preço do livro: "))
        self.preco = novoValor
        return self.preco
    
    def desconto(self,percentualAumento):
        valor = float(self.preco)  - float(self.preco)*(percentualAumento)
        print("O novo preco = ",valor)

livro = Livro("Menino Baleia","40","Lulu Lima",52.9)
livro.getPreco()
print("Valor Novo = ",livro.setPreco())

aux = float(input("Digite o percentual de desconto: "))
livro.desconto(aux)

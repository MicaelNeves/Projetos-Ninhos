class Pokemon:
    def __init__(self,especie, tipo, hp,atk, defesa,vantagem):
        self.especie = especie
        self.tipo = tipo
        self.hp = float(hp)
        self.atk = float(atk)
        self.defesa = float(defesa)
        self.vantagem = float(vantagem)

    def batalha(self):     
        pass


class PokemonAquatico(Pokemon):
    def __init__(self, especie, tipo, hp, atk, defesa,vantagem):
        super().__init__(especie, tipo, hp, atk, defesa, vantagem)

    def Vantagem(self):
        self.vantagem = 1
        match self.tipo:
            case 'Fogo':
                self.vantagem = 1.20
            case 'Agua':
                self.vantagem = 1.00
            case 'Eletrico':
                self.vantagem = 0.80

    def batalha(self,oponente):
        poder = (self.atk + self.defesa + self.hp)*self.vantagem
        poderOponente = (oponente.atk + oponente.defesa + oponente.hp)*self.vantagem

        if poder>poderOponente: 
            print(f"{self.especie} ganhou com {poder}")
        else:
            print(f"{oponente.especie} ganhou com poder {poderOponente}")       
    



class PokemonFogo(Pokemon):
    def __init__(self, especie, tipo, hp, atk, defesa,vantagem):
        super().__init__(especie, tipo, hp, atk, defesa,vantagem)

    def Vantagem(self):
        self.vantagem = 1
        match self.tipo:
            case 'Fogo':
                self.vantagem = 1.00
            case 'Agua':
                self.vantagem = 0.70
            case 'Eletrico':
                self.vantagem = 1.10

    def batalha(self,oponente):
        poder = (self.atk + self.defesa + self.hp)*self.vantagem
        poderOponente = (oponente.atk + oponente.defesa + oponente.hp)*self.vantagem

        if poder>poderOponente: 
            print(f"{self.especie} ganhou com {poder}")
        else:
            print(f"{oponente.especie} ganhou com poder {poderOponente}")       
        
       


class PokemonEletrico(Pokemon):
    def __init__(self, especie, tipo, hp, atk, defesa,vantagem):
        super().__init__(especie, tipo, hp, atk, defesa,vantagem)

    def Vantagem(self):
        self.vantagem = 1
        match self.tipo:
            case 'Fogo':
                self.vantagem = 0.90
            case 'Agua':
                self.vantagem = 1.30
            case 'Eletrico':
                self.vantagem = 1.00

    def batalha(self,oponente):
        poder = (self.atk + self.defesa + self.hp)*self.vantagem
        poderOponente = (oponente.atk + oponente.defesa + oponente.hp)*self.vantagem

        if poder>poderOponente: 
            print(f"{self.especie} ganhou com {poder}")
        else:
            print(f"{oponente.especie} ganhou com poder {poderOponente}")       
        

    
'''
import random

if __name__ == "__main__":

    pokemon1 = PokemonEletrico("Pikachu","Eletrico","45","60","80",0)
    pokemon2 = PokemonFogo("Charmander","Fogo","39","50","52",0)
    pokemon3 = PokemonAquatico("Squirty","Agua","35","28","45",0)  
    print(pokemon1.especie,"-",pokemon1.tipo)
    print(pokemon2.especie,"-",pokemon2.tipo)
    print(pokemon3.especie,"-",pokemon3.tipo)
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
    
    print("você escolheu ",pokemonEscolhido.especie)
    pokemonOponente = random.choice([pokemon1,pokemon2,pokemon3])
    
    print(pokemonOponente.__dict__)
    pokemonEscolhido.Vantagem()
    pokemonEscolhido.batalha(pokemonOponente)


'''

        
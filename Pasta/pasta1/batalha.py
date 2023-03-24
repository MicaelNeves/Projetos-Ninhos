from classPokemon import *
import random

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
    
print("O oponente escolheu: ",pokemonOponente.especie)
pokemonEscolhido.Vantagem()
pokemonEscolhido.batalha(pokemonOponente)
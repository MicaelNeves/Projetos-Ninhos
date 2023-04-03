from classpokemon import *
import pokedex

# Tela principal do jogo

print("=============================================")
print("===BEM-VINDO AO MARAVILHOSO MUNDO POKEMON====")
print("=============================================")
nomeJogador = input("Digite seu nome: ")   # Nome do Jogador


while True:
    print("############################################")
    print("Olá, eu sou o Prof. Oak! Um mundo de batalhas e aventuras o espera.Porém, antes disso,")
    print("você pricisar decidir qual amigo pokemon você quer que o  acompanhe!")
    # Pokemons Iniciais já estabelecidos
    print('''
    Escolha seu Pokemon inicial:
    1. Bulbasauro
    4. Charmander
    7. Squirtle
    ''')

    meuPokemonInicial = int(input("Digite o numero do pokemon escolhido: "))

    if meuPokemonInicial in (1, 4, 7):
        inicial = objPokemon(meuPokemonInicial)
        print("Boa Escolha! Você agora possui o ", inicial._especie)
        break
    else:
        print("Você precisa digitar um opção válida, Tente novamente!")

a = 1    # Auxiliar que funcinar como auxiliar Global

# Modela objeto orientado Jogador

jogador = Jogador(nomeJogador, [objPokemon(meuPokemonInicial)])
print("========================================")
nomeInimigo = input("Digite o nome do seu rival: ")


# Modela objeto orientado Inimigo

listaInimigo = [objPokemon(random.randint(1, 151)), objPokemon(random.randint(1, 151)), objPokemon(random.randint(
    1, 151)), objPokemon(random.randint(1, 151)), objPokemon(random.randint(1, 151)), objPokemon(random.randint(1, 151))]
inimigo = Inimigo(nomeInimigo, listaInimigo)
print(f"Seu rival {nomeInimigo} possui em sua equipe: ")
print(inimigo.listaPokemon())


while True:
    print("========================================")
    print("Comece sua aventura, escolhendo uma ação abaixo")
    print('''
    
    1. Ver lista de Pokemons
    2. Batalhar contra Rival
    3. Ver lista Pokemon de seu Rival
    4. Capturar Pokemon
    5. Aumente o poder de ataque para 100 de um de seus pokemons (Rare Candy)
    6. Sair do Jogo
    
    ''')

    aux = input("Digite o que deseja fazer agora: ")

    # Seleções para definir quais procedimentos utilizados
    # utiliza em funções modeladas nas classes

    match aux:
        case "1":
            print("=============================================")
            jogador.listaPokemon()
            print("=============================================")
        case "2":
            print("=============================================")
            batalhaPokemon(jogador, inimigo,
                           jogador.escolhaPokemon(), inimigo.escolhaPokemon())
            print("=============================================")
        case "3":
            print("=============================================")
            inimigo.listaPokemon()
            print("=============================================")
        case "6":
            print("Você escolheu sair do jogo!")
            break
        case "4":
            jogador.capturarPokemon()
        case "5":
            pass
        case _:
            print("Você escolheu uma opção inválida, insira novamente!")
            break

    # Pocedimento obrigatorio para colocar um unico laço de repetição

    if aux == "5" and a == 1:
        jogador.aumentarAtaque()
        a += 1
    elif aux == "5" and a != 1:
        print(f"Você já realizou o aumento de ataque")

    # Se o Adversário não possuir mais pokemons em seu time
    # O jogo encerra-se através dessa estrutrua de decisão

    if listaInimigo == []:
        print(f"{inimigo.nome} não possui mais pokemon!")
        print(f"{jogador.nome} Venceu o jogo")
        print("=============================================")
        print("   ================PARABÉNS===============   ")
        print("=============================================")
        break
    input("Digite Enter para continuar.")

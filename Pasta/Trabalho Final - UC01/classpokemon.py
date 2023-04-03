
import pokedex
import random

# Criação de classe Pokemon e subclasses em relação ao tipo


class Pokemon:
    def __init__(self, especie, tipo, ataque, defesa, hp):
        self._especie = especie
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._hp = hp
        self._desvantagens = []
        self._vantagens = []

    # checa vantagens em relação ao time dos pokemons adversários

    def checar_vantagem(self, time_inimigo):
        if time_inimigo._tipo in self._vantagens:
            return 2
        elif time_inimigo._tipo in self._desvantagens:
            return 0.5
        else:
            return 1


class Agua(Pokemon):
    def __init__(self, especie, tipo, ataque, defesa, hp):
        super().__init__(especie, tipo, ataque, defesa, hp)
        self._vantagens = ['fogo']
        self._desvantagens = ['grama']


class Fogo(Pokemon):
    def __init__(self, especie, tipo, ataque, defesa, hp):
        super().__init__(especie, tipo, ataque, defesa, hp)
        self._vantagens = ['grama']
        self._desvantagens = ['agua']


class Grama(Pokemon):
    def __init__(self, especie, tipo, ataque, defesa, hp):
        super().__init__(especie, tipo, ataque, defesa, hp)
        self._vantagens = ['agua']
        self._desvantagens = ['fogo']


class Normal(Pokemon):
    def __init__(self, especie, tipo, ataque, defesa, hp):
        super().__init__(especie, tipo, ataque, defesa, hp)
        self._vantagens = ['fantasma']
        self._desvantagens = ['eletrico']


class Eletrico(Pokemon):
    def __init__(self, especie, tipo, ataque, defesa, hp):
        super().__init__(especie, tipo, ataque, defesa, hp)
        self._vantagens = ['agua']
        self._desvantagens = ['fantasma']


class Psiquico(Pokemon):
    def __init__(self, especie, tipo, ataque, defesa, hp):
        super().__init__(especie, tipo, ataque, defesa, hp)
        self._vantagens = ['venenoso']
        self._desvantagens = ['fantasma', 'inseto']


class Fantasma(Pokemon):
    def __init__(self, especie, tipo, ataque, defesa, hp):
        super().__init__(especie, tipo, ataque, defesa, hp)
        self._vantagens = ['psiquico']
        self._desvantagens = ['fantasma']


class Venenoso(Pokemon):
    def __init__(self, especie, tipo, ataque, defesa, hp):
        super().__init__(especie, tipo, ataque, defesa, hp)
        self._vantagens = ['grama']
        self._desvantagens = ['psiquico']


class Inseto(Pokemon):
    def __init__(self, especie, tipo, ataque, defesa, hp):
        super().__init__(especie, tipo, ataque, defesa, hp)
        self._vantagens = ['grama']
        self._desvantagens = ['fogo']

# Modelar classe Treinador com subclasses Jogador e Inimigo


class Treinador:
    def __init__(self, nome, time):
        self.nome = nome
        self._time = time

    # Funções principais em escolher pokemon, adicionar, lista, capturar

    def escolhaPokemon(self):
        return random.choice(self._time)

    def adicionarpokemon(self, novo):
        return self._time.append(novo)

    def listaPokemon(self):
        print("Nº |   Nome |   Tipo | Ataque |  Defesa  |   HP")
        i = 1
        for pokemon in self._time:
            print(
                f"{i}  |  {pokemon._especie} | {pokemon._tipo}  |  {pokemon._ataque}  | {pokemon._defesa}   | {pokemon._hp}")
            i += 1

    def capturarPokemon(self):

        pokemonEscolhido = random.choice(pokedex.pokemons)

        print(
            f"Foi encontrando um {pokemonEscolhido['nome']} - {pokemonEscolhido['tipo']} ")

        pokemonRepetido = False

        for pokemon in self._time:
            if pokemonEscolhido['nome'] == pokemon._especie:
                pokemonRepetido = True

        if pokemonRepetido:
            print("Este Pokemon já está no time")
        else:
            match pokemonEscolhido["tipo"]:
                case "agua":
                    objPokemon = Agua(pokemonEscolhido["nome"], pokemonEscolhido["tipo"],
                                      pokemonEscolhido["ataque"], pokemonEscolhido["defesa"], pokemonEscolhido["hp"])
                case "fogo":
                    objPokemon = Fogo(pokemonEscolhido["nome"], pokemonEscolhido["tipo"],
                                      pokemonEscolhido["ataque"], pokemonEscolhido["defesa"], pokemonEscolhido["hp"])
                case "grama":
                    objPokemon = Grama(pokemonEscolhido["nome"], pokemonEscolhido["tipo"],
                                       pokemonEscolhido["ataque"], pokemonEscolhido["defesa"], pokemonEscolhido["hp"])
                case "eletrico":
                    objPokemon = Eletrico(pokemonEscolhido["nome"], pokemonEscolhido["tipo"],
                                          pokemonEscolhido["ataque"], pokemonEscolhido["defesa"], pokemonEscolhido["hp"])
                case "fantasma":
                    objPokemon = Fantasma(pokemonEscolhido["nome"], pokemonEscolhido["tipo"],
                                          pokemonEscolhido["ataque"], pokemonEscolhido["defesa"], pokemonEscolhido["hp"])
                case "venenoso":
                    objPokemon = Venenoso(pokemonEscolhido["nome"], pokemonEscolhido["tipo"],
                                          pokemonEscolhido["ataque"], pokemonEscolhido["defesa"], pokemonEscolhido["hp"])
                case "normal":
                    objPokemon = Normal(pokemonEscolhido["nome"], pokemonEscolhido["tipo"],
                                        pokemonEscolhido["ataque"], pokemonEscolhido["defesa"], pokemonEscolhido["hp"])
                case "psiquico":
                    objPokemon = Psiquico(pokemonEscolhido["nome"], pokemonEscolhido["tipo"],
                                          pokemonEscolhido["ataque"], pokemonEscolhido["defesa"], pokemonEscolhido["hp"])
                case "inseto":
                    objPokemon = Inseto(pokemonEscolhido["nome"], pokemonEscolhido["tipo"],
                                        pokemonEscolhido["ataque"], pokemonEscolhido["defesa"], pokemonEscolhido["hp"])
                case _:
                    objPokemon = Pokemon(pokemonEscolhido["nome"], pokemonEscolhido["tipo"],
                                         pokemonEscolhido["ataque"], pokemonEscolhido["defesa"], pokemonEscolhido["hp"])

            meupokemon = self.escolhaPokemon()
            if meupokemon._ataque >= objPokemon._ataque:
                self._time.append(objPokemon)
                print(objPokemon._especie, "Agora faz parte do time!")
            else:
                print("Falha na capturar", objPokemon._especie)


class Jogador(Treinador):
    def __init__(self, nome, time):
        super().__init__(nome, time)

    # Funções para escolher pokemon de um menu pré-estabelecido

    def escolhaPokemon(self):

        self.listaPokemon()

        aux = int(input("Digite o numero do Pokemon: "))

        meuPokemon = self._time[aux-1]

        return meuPokemon

    # Aumentar ataque do pokemon do Jogador

    def aumentarAtaque(self):

        self.listaPokemon()
        aux = int(input("Digite o numero do pokemon p/ aumentar ataque : "))
        pokemonEscolhido = self._time[aux - 1]
        pokemonEscolhido._ataque = 100
        print("Aumento de Ataque Realizado.")
        print(pokemonEscolhido.__dict__)
        print("Continue sua Jornada Pokemon!")


class Inimigo(Treinador):
    def __init__(self, nome, time):
        super().__init__(nome, time)

    def listaPokemon(self):
        print("Nº |   Nome |   Tipo | Ataque |  Defesa  |   HP")
        i = 1
        for pokemon in self._time:
            print(
                f"{i}  |  {pokemon._especie} | {pokemon._tipo}  |  {pokemon._ataque}  | {pokemon._defesa}   | {pokemon._hp}")
            i += 1


# Modelar Função para Método de Batalha

def batalhaPokemon(jogador, inimigo, pokemon1, pokemon2):

    # Checar vantagem para o uso no metodo

    vantagem = pokemon1.checar_vantagem(pokemon2)
    desvantagem = pokemon2.checar_vantagem(pokemon1)

    print(f"Você escolheu {pokemon1._especie}")

    print(f"O Inimigo escolheu {pokemon2._especie}")

    # O metodo escolhido usa a diferença entre a vantagem relativa ao ataque do pokemon
    # e a defesa do pokemon adversário

    poder1 = (vantagem*pokemon1._ataque - pokemon2._defesa)
    poder2 = (desvantagem*pokemon2._ataque - pokemon1._defesa)
    print(f"Poder do seu pokemon: ", poder1)
    print(f"Poder do inimigo: ", poder2)

    # Metodo de Batalha

    if poder1 > poder2:
        # Se o jogador ganhar pode optar por adicionar o pokemon adversário ao seu time
        print(f"{pokemon1._especie} ganhou!")
        aux = input(
            f"Você desejar adquirir {pokemon2._especie} - {pokemon2._tipo}?[S][N]: ")
        if aux.upper() == 'S':
            print("=============================================")
            # Adionar o pokemon adversário no  time do Jogador
            jogador.adicionarpokemon(pokemon2)
            print(pokemon2._especie, " Agora faz parte de seu time!")
            # Remove o pokemon adversário do seu time
            inimigo._time.remove(pokemon2)
            print(f"Seu rival {inimigo.nome} possui em sua equipe: ")
            print(inimigo.listaPokemon())
            return True
        elif aux.upper() == 'N':
            print("=============================================")
            print("Você não tem interrese no pokemon adversario!")
            # Se o Jogador ganhar e decidir por não querer o pokemon adversário será direcionado para captura pokemon
            print("Então, capture um novo ppkemon!!!")
            print("=============================================")
            jogador.capturarPokemon()
            print(jogador.listaPokemon())
            return True
        else:
            print("Erro na verificação")
            return True
    elif poder1 < poder2:
        print(f"{pokemon2._especie} ganhou!")
        # Se o Inimigo ganhar será direcionado para capturar de um novo pokemon
        print(f"{inimigo.nome} vai tentar capturar um novo pokemon")
        inimigo.capturarPokemon()
        print(inimigo.listaPokemon())
        return False
    elif poder1 == poder2:
        print("Deu empate")
        return False
    else:
        print("Algo não saiu como esperado")


# Funções para criar objeto orientado Pokemon

def objPokemon(numeroPok):

    meuPokemon = pokedex.pokemons[numeroPok-1]
    match meuPokemon["tipo"]:
        case "agua":
            objPokemon = Agua(meuPokemon["nome"], meuPokemon["tipo"],
                              meuPokemon['ataque'], meuPokemon['defesa'], meuPokemon['hp'])
        case "fogo":
            objPokemon = Fogo(meuPokemon["nome"], meuPokemon["tipo"],
                              meuPokemon['ataque'], meuPokemon['defesa'], meuPokemon['hp'])
        case "eletrico":
            objPokemon = Eletrico(meuPokemon["nome"], meuPokemon["tipo"],
                                  meuPokemon['ataque'], meuPokemon['defesa'], meuPokemon['hp'])
        case "venenoso":
            objPokemon = Venenoso(meuPokemon["nome"], meuPokemon["tipo"],
                                  meuPokemon['ataque'], meuPokemon['defesa'], meuPokemon['hp'])
        case "fantasma":
            objPokemon = Fantasma(meuPokemon["nome"], meuPokemon["tipo"],
                                  meuPokemon['ataque'], meuPokemon['defesa'], meuPokemon['hp'])
        case "normal":
            objPokemon = Normal(meuPokemon["nome"], meuPokemon["tipo"],
                                meuPokemon['ataque'], meuPokemon['defesa'], meuPokemon['hp'])
        case "psiquico":
            objPokemon = Psiquico(meuPokemon["nome"], meuPokemon["tipo"],
                                  meuPokemon['ataque'], meuPokemon['defesa'], meuPokemon['hp'])
        case "inseto":
            objPokemon = Inseto(meuPokemon["nome"], meuPokemon["tipo"],
                                meuPokemon['ataque'], meuPokemon['defesa'], meuPokemon['hp'])
        case "grama":
            objPokemon = Grama(meuPokemon["nome"], meuPokemon["tipo"],
                               meuPokemon['ataque'], meuPokemon['defesa'], meuPokemon['hp'])
    return objPokemon

class Animal:
    def __init__(self,nome,cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"{self.nome} esta comendo")


class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)




if __name__ == '__main__':

    cachorro = Cachorro("Pluto","Amarelo")
    cachorro.comer()

    gato = Gato("Yoruichi","Preto")
    gato.comer()

    coelho = Coelho("Pluto","Amarelo")
    coelho.comer()
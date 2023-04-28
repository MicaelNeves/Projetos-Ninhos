import psycopg2
from Controle.classControle import Conexao
from  Modelo.classAluguel import Aluguel
from Modelo.classCliente import Cliente
from Modelo.classLivro import Livro


conexaoLivraria = Conexao("ABC Livraria", "localhost", "5432", "postgres", "postgres")

def cadastroLivro():

    print("=====INICIALIZANDO CADASTRO=======")

    livro = Livro(None, input("Digite o título do livro: "),input("Digite o autor do livro: "),input("Digite o preco do livro: "),input("Digite a quantidade no estoque livro: "))
    conexaoLivraria.manipularBanco(livro.inserirLivro())

    print("=======CADASTRO REALIZADO=========")

def cadastroCliente():
     
    print("=====INICIALIZANDO CADASTRO=======")

    cliente = Cliente(None, input("Digite o nome do cliente: "),input("Digite o CPF do cliente: "))
    conexaoLivraria.manipularBanco(cliente.inserirCliente())

    print("=======CADASTRO REALIZADO=========")

def cadastroAluguel():

    print("=====INICIALIZANDO CADASTRO=======")

    aluguel = Aluguel(None,None, None, )
    conexaoLivraria.manipularBanco(aluguel.inserirAluguel())

    print("=======CADASTRO REALIZADO=========")


def CriarTabelas(aux):

    while aux<2:
        try: 
            conexaoLivraria.manipularBanco(Aluguel. criarTabelaAluguel())
            conexaoLivraria.manipularBanco(Cliente. criarTabelaCliente())
            conexaoLivraria.manipularBanco(Livro. criarTabelaLivro())
            print("Tabelas Criadas com sucesso!")
        except(Exception,psycopg2.Error) as error:
            print("Algo deu Errado! ",error)

        aux += 1

CriarTabelas(1)

def TelaPrincipal():
    
    while True:
        print('''
        ===============================
            BEM-VINDO ABC LIVRARIA
        -----======================----

        Qual operação você desejar realizar?

        1. Cadastro de Livros
        2. Cadastro de Clientes
        3. Cadastro de Aluguel de Livro
        4. Visualisar Livros do Catalogo
        5. Visualizar Clientes assinantes
        6. Visualisar aluguéis realizados
        7. Sair

        ''')

        op = input("Digite a ação que deseja realizar? ")

        match op:
            case "1":
                cadastroLivro()
            case "2":
                cadastroCliente()
            case "3":
              #  cadastroAluguel()
              pass
            case "4":
                pass
            case "6":
                pass
            case "7":
                print("Voce Finalizou a consulta!")
                break
            


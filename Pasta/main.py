from  Controle.classConexao import Conexao
from Modelo.classCliente import Cliente
import psycopg2

conexaoBanco = Conexao("Empresa3", "localhost", "5432","postgres", "postgres")

def inserirCliente():

        print("===========Cadastro de Cliente======")
        cliente = Cliente('default', input("Digite o nome do cliente: "))

        
        conexaoBanco.manipularBanco(cliente.inserircliente())
        print("Cliente Cadastrado")




    
while True:
        try:
               
            print('''

            BEM_VINDO A LOJA 

            INDIQUE A OPERACAO A SER REALIZADA:
            1- Cadastrar Cliente
            2- Cadastrar Produto
            3- Cadastrar Compra
            4- Sair

            ''')
            op = int(input("Digite a opcao desejada: "))

            match op:
                  case 1:
                        inserirCliente()
                  case 2:
                        pass
                  case 3:
                        pass
                  case 4:
                        pass
                  case _:
                        print("Você precisa digitar uma opção válida!")

            pass 

    # inserirCliente()

        except(Exception, psycopg2.Error) as error:
            print("Ocorreu um erro!", error)




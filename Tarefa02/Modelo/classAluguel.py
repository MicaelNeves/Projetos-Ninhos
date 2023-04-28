class Aluguel:
    def __init__(self,id_aluguel,id_cliente, id_produto, nome_produto, quantidade,preco_final, hora):
        self._id_aluguel = id_aluguel
        self._id_cliente = id_cliente
        self._id_produto = id_produto
        self._nome_produto = nome_produto
        self._quantidade = quantidade
        self._preco_final = preco_final
        self._hora = hora
    

    def criarTabelaAluguel():
        sql = '''
        CREATE TABLE "Aluguel"(
        "Id_Aluguel" int GENERATED ALWAYS IDENTITY PRIMARY KEY,
        "Id_Cliente" int,
        "Id_Produto" int,
        "Nome_Produto" varchar(255) NOT NULL,
        "Quantidade" int NOT NULL default 1,
        "Preço_Total" numeric NOT NULL,
        "Hora da Aluguel" timestamp default CURRENT_TIMESTAMP(0),
        CONSTRAINT fk_cliente
            FOREIGN KEY("Id_Cliente")
            REFERENCES "Cliente"("Id_Cliente")
            ,
        CONSTRAINT fk_livro
            FOREIGN KEY("Id_Produto")
            REFERENCES "Catalogo"("Id_Livro")
        )
        '''
        return sql
    
    def inserirAluguel(self):

        sql = f'''
        INSERT INTO "Livro"
        values({self._id_aluguel}, {self._id_cliente},{self._id_produto}'{self._nome_produto}','{self._quantidade},'{self._preco_final}','{self._hora}')
        '''
        return sql


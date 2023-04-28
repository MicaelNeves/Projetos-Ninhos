class Livro: 

    def __init__(self,id_Livro,titulo,autor,preco,estoque):
        self._id_Livro = id_Livro
        self._titulo = titulo
        self._autor = autor
        self._preco = preco
        self._estoque = estoque
        
    def criarTabelaLivro():
        sql = '''
        CREATE TABLE "Catalogo"(
        "Id_Livro" int GENERATED ALWAYS IDENTITY PRIMARY KEY,
        "Titulo" varchar(255) NOT NULL,
        "Autor" varchar(11) NOT NULL,
        "Preço" numeric NOT NULL default, 
        "Estoque" numeric NOT NULL default
        )
        '''
        return sql
    
    def inserirLivro(self):
        sql = f'''
        INSERT INTO "Livro"
        values({self._id_Livro},'{self._titulo}','{self._autor},'{self._preco}','{self._estoque}')
        '''
        return sql
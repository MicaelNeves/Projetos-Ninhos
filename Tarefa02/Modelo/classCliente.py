class Cliente: 
    def __init__(self,nome, cpf):
        self._nome= nome
        self._cpf = cpf


    def criarTabelaCliente():
        sql = '''
        CREATE TABLE "Cliente"(
        "Id_Cliente" int GENERATED ALWAYS IDENTITY PRIMARY KEY,
        "Nome" varchar(255) NOT NULL,
        "CPF" varchar(11) NOT NULL,
        )
        '''
        return sql
    
    def inserirCliente(self):
        sql = f'''
        INSERT INTO "Cliente"
        values(default, '{self._nome}','{self._cpf}')
        '''
        return sql
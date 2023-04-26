class Cliente:
    def __init__(self,id, nome):
        self._nome = nome
        self._id = id

    def inserircliente(self):

        sql = f'''
        INSERT INTO "Cliente"
        VALUES (default, '{self._nome}')
        '''

        return sql
    

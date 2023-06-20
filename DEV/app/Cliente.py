class Cliente:
    def __init__(self, n, fone):

        self._nome = n
        self._telefone = fone

    #MÉTODO GET
    def get_nome(self):
        return self._nome
    #MÉTODO SET
    def set_nome(self, _nome):
        self._nome = _nome
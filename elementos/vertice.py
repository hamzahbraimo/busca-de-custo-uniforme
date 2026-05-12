class Vertice:

    def __init__(self, nome: str, objectivo: bool):
        self.nome = nome
        self.objectivo = objectivo

    def get_nome(self):
        return self.nome
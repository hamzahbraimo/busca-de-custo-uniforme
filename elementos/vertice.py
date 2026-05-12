class Vertice:

    def __init__(self, nome: str, objectivo: bool):
        self.nome = nome
        self.objectivo = objectivo
        self.inicial: bool | bool = False

    def nome(self):
        return self.nome

    def __lt__(self, outro):
        return self.nome < outro.nome
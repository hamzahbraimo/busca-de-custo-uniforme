from elementos.vertice import Vertice


class Aresta:

    def __init__(self, origem: Vertice, destino: Vertice, peso: int):
        self.origem = origem
        self.destino = destino
        self.peso = peso

    def origem(self) -> Vertice:
        return self.origem

    def destino(self) -> Vertice:
        return self.destino

    def peso(self) -> int:
        return self.peso

    def link(self) -> str:
        return f"{self.origem} ---({self.peso})---> {self.destino}"
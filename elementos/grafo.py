from elementos.aresta import Aresta
from elementos.vertice import Vertice


class Grafo:
    def __init__(self):
        self.adjacencias:  dict [Vertice, list[Aresta]] = {}
        self.numero_arestas = 0

    def add_vertice(self, v: Vertice):
        if v not in self.adjacencias:
            self.adjacencias[v] = []

    def existe_aresta(self, origem: Vertice, destino: Vertice) -> bool:
        for a in self.adjacencias[origem]:
            if a.destino is destino:
                return True

        return False

    def add_aresta(self, origem: Vertice, destino: Vertice, peso: int) -> None:
        if peso < 0:
            print(f'Custo de caminho nao pode ser negativo ({peso})')
            return

        if self.numero_arestas > 0:
            if self.existe_aresta(origem, destino):
                print(f"Ja existe uma aresta entre {origem.nome} e {destino.nome}")
                return
        else:
            origem.inicial = True


        self.add_vertice(origem)
        self.add_vertice(destino)

        self.adjacencias[origem].append(Aresta(origem, destino, peso))
        self.adjacencias[destino].append(Aresta(destino, origem, peso)) # bidirecional
        self.numero_arestas += 1

    def tem_objectivo(self) -> bool:
        for v in self.adjacencias:
            if v.objectivo:
                return True

        return False

    def tem_inicial(self) -> bool:
        for v in self.adjacencias:
            if v.inicial:
                return True

        return False

    # def imprimir_grafo(self) -> None:
    #     if not self.contem_objectivo():
    #         print('Nao existe estado objectivo')
    #         return
    #
    #     for v in self.adjacencias:
    #         if v.inicial:
    #             print(f"*{v.nome} --> ", end=" ")
    #         elif v.objectivo:
    #             print(f"{v.nome}* --> ", end=" ")
    #         else:
    #             print(f"{v.nome} --> ", end=" ")
    #
    #         for a in self.adjacencias[v]:
    #             if a.destino.objectivo:
    #                 print(f"{a.destino.nome}({a.peso})*", end=" ")
    #             else:
    #                 print(f"{a.destino.nome}({a.peso})", end=" ")
    #         print()

    def inicial(self) -> Vertice | None:

        for v in self.adjacencias:
            if v.inicial:
                return v

        return None

    def objectivo(self) -> Vertice | None:

        for v in self.adjacencias:
            if v.objectivo:
                return v
        return None
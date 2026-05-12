import heapq
from elementos.grafo import Grafo
from elementos.vertice import Vertice


class BCU:

    def __init__ (self):
        self.lista = []

    def arestas_to_list(self, grafo: Grafo) -> list[dict]:

        for v in grafo.adjacencias:
            for a in grafo.adjacencias[v]:
                self.lista.append({
                    "origem": v.nome,
                    "destino": a.destino.nome,
                    "peso": a.peso
                })
        return self.lista



    def bcu(self, grafo: Grafo, inicio: Vertice, objectivo: Vertice):
        expansao = [(0, inicio, [inicio])]
        visitados = set()

        while expansao:
            custo, vertice, caminho = heapq.heappop(expansao)

            if vertice == objectivo:
                return caminho, custo

            if vertice in visitados:
                continue

            visitados.add(vertice)

            for aresta in grafo.adjacencias[vertice]:
                novo_custo = custo + aresta.peso
                heapq.heappush(
                    expansao,
                    (novo_custo, aresta.destino, caminho + [aresta.destino])
                )
        return None
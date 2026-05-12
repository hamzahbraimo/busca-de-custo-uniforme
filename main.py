from elementos.grafo import Grafo
from elementos.vertice import Vertice

gr = Grafo()

a = Vertice("A", False)
b = Vertice("B", False)
c = Vertice("C", True)

gr.add_aresta(a, b, 3)
gr.add_aresta(a, c, 4)
gr.add_aresta(b, c, 5)

print(a.inicial)

gr.imprimir_grafo()
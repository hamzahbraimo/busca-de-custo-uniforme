from elementos.grafo import Grafo
from elementos.vertice import Vertice

gr = Grafo()

a = Vertice("A")
b = Vertice("B")
c = Vertice("C")

gr.add_aresta(a, b, 3)
gr.add_aresta(a, c, 4)
gr.add_aresta(b, c, 5)

gr.imprimir_grafo()
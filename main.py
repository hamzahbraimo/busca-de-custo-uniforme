from bcu.busca_custo_uniforme import BCU
from elementos.grafo import Grafo
from elementos.vertice import Vertice
import random

gr = Grafo()

a = Vertice("1", False)
b = Vertice("2", False)
c = Vertice("3", False)
d = Vertice("4", False)
e = Vertice("5", False)
f = Vertice("6", True)

gr.add_aresta(a, b, 21)
gr.add_aresta(a, c, 13)
gr.add_aresta(b, c, 23)
gr.add_aresta(b, d, 42)
gr.add_aresta(c, d, 34)
gr.add_aresta(c, e, 35)
gr.add_aresta(d, e, 54)
gr.add_aresta(d, f, 64)

if gr.tem_inicial() and gr.tem_objectivo():
    bcu = BCU()

    caminho, custo = bcu.bcu(gr, gr.inicial(), gr.objectivo())

    print('Caminho:')
    for v in caminho:
        print(f"{v.nome} ->", end=" ")

    print(f'Custo: {custo}')
else:
    print('Nao existe estado inicial ou objectivo')
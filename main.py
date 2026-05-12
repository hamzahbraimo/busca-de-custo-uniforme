from bcu.busca_custo_uniforme import BCU
from elementos.grafo import Grafo
from elementos.vertice import Vertice

gr = Grafo()

a = Vertice("A", False)
b = Vertice("B", False)
c = Vertice("C", True)
d = Vertice("D", False)
#
gr.add_aresta(a, b, 10)
gr.add_aresta(a, c, 18)
gr.add_aresta(a, d, 6)
gr.add_aresta(b, c, 1)
gr.add_aresta(d, c, 3)

if gr.tem_inicial() and gr.tem_objectivo():
    bcu = BCU()

    caminho, custo = bcu.bcu(gr, gr.inicial(), gr.objectivo())

    print('Caminho:')
    for v in caminho:
        print(f"{v.nome} ->", end=" ")

    print(f'Custo: {custo}')
else:
    print('Nao existe estado inicial ou objectivo')
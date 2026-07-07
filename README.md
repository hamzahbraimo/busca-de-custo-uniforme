# BUSCA DE CUSTO UNIFORME
*Uniform-Cost Search* é um algoritmo de busca cega que encontra o caminho de menor custo total em um grafo ponderado. Ele prioriza a expansão do nó com a menor distância acumulada desde a origem, similar ao `Algoritmo de Dijkstra`.

***
# Como funciona
1. Remove o nó com o menor custo acumulado da fronteira;
2. Verifica se o nó é o objetivo desejado;
3. Se não for, ele expande esse nó, calcula o custo para chegar aos seus vizinhos e os adiciona à fronteira;
4. Repete o processo mantendo a fila ordenada pelo custo total.

***
# Características
- **Optimalidade:** sempre encontra o caminho de menor custo.
- **Completude:** Se o caminho mínimo tiver um custo finito e o factor de ramificação for finito, o objetivo será encontrado.
- **Limitações:** pode falhar ou entrar em loop infinito se o grafo tiver ciclos com custo menor ou igual a zero.

***
# Exemplo de implementação
```
# Dentro do main.py

a = Vertice("1", False) # nome, estado objectivo ou nao
b = Vertice("2", False)
c = Vertice("3", False)
d = Vertice("4", False)
e = Vertice("5", False)
f = Vertice("6", True) # Estado objectivo

gr.add_aresta(a, b, 21) # nó  origem, nó  destino, peso
gr.add_aresta(a, c, 13)
gr.add_aresta(b, c, 23)
gr.add_aresta(b, d, 42)
gr.add_aresta(c, d, 34)
gr.add_aresta(c, e, 35)
gr.add_aresta(d, e, 54)
gr.add_aresta(d, f, 64)
```

Visualmente:
<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/00187470-ecc1-415f-ba0a-b9af65629110" />

Para este grafo, iria percorrer o caminho `1 -> 3 -> 4 -> 6` com um custo total de `111`.

***
# Referências
- https://www.youtube.com/watch?v=IeE_5cMlrkE
- https://www.youtube.com/watch?v=j5ab53LQkO0

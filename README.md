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
- **Optimalidade:**
- **Completude:**
- **Complexidade no pior caso:**
- **Limitações:** pode falhar ou entrar em loop infinito se o grafo tiver ciclos com custo menor ou igual a zero.

***
# Referências
- https://www.youtube.com/watch?v=IeE_5cMlrkE
- https://www.youtube.com/watch?v=j5ab53LQkO0

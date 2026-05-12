from classes.tree import Tree

av = Tree()
av.add("A", -1) # raiz
av.add("B", 3)
av.add("C", 4)
av.add("D", 5)

print(av.dfs()) # listagem da arvore
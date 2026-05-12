from classes.node import Node
from collections import deque

class Tree:

    def __init__(self):
        self.size: int = 0
        self.root: Node | None = None

    def add_node(self, parent: Node, name: str, cost: int):
        if name == parent.name:
            print('Nao pode ter elementos duplicados')
            return

        if name < parent.name:
            if parent.left is None:
                parent.left = Node(name)
                parent.children += 1
            else:
                self.add_node(parent.left, name, cost)
        else:
            if parent.right is None:
                parent.right = Node(name)
                parent.children += 1
            else:
                self.add_node(parent.right, name, cost)



    def add(self, name: str, cost: int):
        if self.root is None:
            self.root = Node(name)
        else:
            self.add_node(self.root, name, cost)

        self.size += 1

    def dfs(self):
        lista = []

        if self.root is None:
            return []

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            lista.append(node.name)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return lista
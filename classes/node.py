class Node:
    def __init__(self, name: str):
        self.name: str = name
        self.left: Node | None = None
        self.right: Node | None = None
        self.children: int = 0
from binary_tree import BinaryTree

tree = BinaryTree()
tree.adicionar(3)
tree.adicionar(4)
tree.adicionar(0)
tree.adicionar(8)
tree.adicionar(2)
tree.printArvore()
print(tree.achar(3).valor)
print(tree.achar(10))
tree.remover()
tree.printArvore()
from binary_tree import BinaryTree

tree = BinaryTree()

tree.adicionar(80)
tree.adicionar(40)
tree.adicionar(10)
tree.adicionar(70)
tree.adicionar(20)
tree.adicionar(50)


tree.print_Arvore("preOrder")
tree.print_Arvore("postOrder")
tree.print_Arvore("inOrder")
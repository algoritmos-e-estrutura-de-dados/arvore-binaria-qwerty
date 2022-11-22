from node import Node

class  BinaryTree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def adicionar(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._adicionar(val, self.root)

    def _adicionar(self, val, node):
        if val < node.valor:
            if node.esquerda is not None:
                self._adicionar(val, node.esquerda)
            else:
                node.esquerda = Node(val)
        else:
            if node.direita is not None:
                self._adicionar(val, node.direita)
            else:
                node.direita = Node(val)


    def preOrder_print(self, começo, string):
        if começo:
            string += (str(começo.value) + "/")
            string = self.preOrder_print(começo.esquerda, string)
            string = self.preOrder_print(começo.direita, string)
        return string

    def inOrder_print(self, string, começo):
        if começo:
            string = self.inOrder_print(começo.esquerda, string)
            string += (str(começo.value) + "-")
            string = self.inOrder_print(começo.direita, string)
        return string

    def postorder_print(self, string, começo):

        if começo:
            string = self.postorder_print(começo.esquerda, string)
            string = self.postorder_print(começo.direita, string)
            string += (str(começo.value) + "-")
        return string


    def printArvore(self):
        if self.root is not None:
            self._printArvore(self.root)


    def _printArvore(self, node):
        if node is not None:
            self._printArvore(node.esquerda)
            print(str(node.valor) + ' ')
            self._printArvore(node.direita)



from node import Node


class BinaryTree:
    def __init__(self):
        self.valor = None
    def getRoot(self):
        return self.root

    def adicionar(self, val):
        if self.esquerda is not None:
            self.adicionar(val, self.esquerda)
        else:
            self.esquerda = Node(val)

        if self.direita is not None:
                self.adicionar(val, self.direita)
        else:
             self.direita = Node(val)

    def preOrder(self, começo, stepe):
        if começo:
            stepe += (str(começo.value) + "/")
            stepe = self.preOrder(começo.esquerda, stepe)
            stepe = self.preOrder(começo.direita, stepe)
        return stepe

    def inOrder(self, stepe, começo):
        if começo:
            stepe = self.inOrder(começo.esquerda, stepe)
            stepe += (str(começo.value) + "/")
            stepe = self.inOrder(começo.direita, stepe)
        return stepe

    def postOrder(self, stepe, começo):
        if começo:
            stepe = self.postOrder(começo.esquerda, stepe)
            stepe = self.postOrder(começo.direita, stepe)
            stepe += (str(começo.value) + "/")
        return stepe

    def remover(self, valor):
        global filho_esquerda
        if self.root == None:
            return False
        atual = self.root
        pai = self.root
        filho_esq = True

        while atual.item != valor:
            pai = atual
            if valor < atual.item:
                atual = atual.esquerda
                filho_esquerda = True
            else:
                atual = atual.direita
                filho_esquerda = False
            if atual == None:
                return False

        if atual.esquerda == None and atual.direita == None:
            if atual == self.root:
                self.root = None
            else:
                if filho_esquerda:
                    pai.esquerda = None
                else:
                    pai.direita = None

        elif atual.direita == None:
            if atual == self.root:
                self.root = atual.esquerda
            else:
                if filho_esquerda:
                    pai.esquerda = atual.esquerda
                else:
                    pai.direita = atual.esquerda

        elif atual.esquerda == None:
            if atual == self.root:
                self.root = atual.direita
            else:
                if filho_esquerda:
                    pai.esquerda = atual.direita
                else:
                    pai.direita = atual.direita

        else:
            sucessor = self.nosucessor(atual)
            if atual == self.root:
                self.root = sucessor
            else:
                if filho_esquerda:
                    pai.esquerda = sucessor
                else:
                    pai.direita = sucessor
            sucessor.esquerda = atual.esquerda

        return True

    def printArvore(self, node):
        if node is not None:
            self.printArvore(node.esquerda)
            print(str(node.valor) + ' ')
            self.printArvore(node.direita)

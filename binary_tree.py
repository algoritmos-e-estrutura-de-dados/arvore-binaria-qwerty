from node1 import Node


class BinaryTree:
    def __init__(self):
        self.raiz = None

        # def raiz(self):
        # self.raiz = None

    def adicionar(self, valor):
        node = Node(valor)

        if self.raiz is None:
            self.raiz = node

        else:
            aux = self.raiz
            pai = None
            while aux is not None:
                if valor == aux.valor:
                    break

                if valor > aux.valor:
                    pai = aux
                    aux = aux.direita
                else:
                    pai = aux
                    aux = aux.esquerda

            if valor > pai.valor:
                pai.direita = node
            else:
                pai.esquerda = node


    def preOrder(self, comeco, stepe):
        if comeco:
            stepe += (str(comeco.valor) + "/")
            stepe = self.preOrder(comeco.esquerda, stepe)
            stepe = self.preOrder(comeco.direita, stepe)
        return stepe


    def inOrder(self, stepe, comeco):
        if comeco:
            stepe = self.inOrder(comeco.esquerda, stepe)
            stepe += (str(comeco.valor) + "/")
            stepe = self.inOrder(comeco.direita, stepe)
        return stepe


    def postOrder(self, stepe, comeco):
        if comeco:
            stepe = self.postOrder(comeco.esquerda, stepe)
            stepe = self.postOrder(comeco.direita, stepe)
            stepe += (str(comeco.valor) + "/")
        return stepe


    def remover(self, val):
        global filho_esquerda
        if self.raiz == None:
            return False
        atual = self.raiz
        pai = self.raiz
        filho_esq = True

        while atual.item != val:
            pai = atual
            if val < atual.item:
                atual = atual.esquerda
                filho_esquerda = True
            else:
                atual = atual.direita
                filho_esquerda = False
            if atual == None:
                return False

        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz:
                self.raiz = None
            else:
                if filho_esquerda:
                    pai.esquerda = None
                else:
                    pai.direita = None

        elif atual.direita == None:
            if atual == self.raiz:
                self.raiz = atual.esquerda
            else:
                if filho_esquerda:
                    pai.esquerda = atual.esquerda
                else:
                    pai.direita = atual.esquerda

        elif atual.esquerda == None:
            if atual == self.raiz:
                self.raiz = atual.direita
            else:
                if filho_esquerda:
                    pai.esquerda = atual.direita
                else:
                    pai.direita = atual.direita

        else:
            sucessor = self.nosucessor(atual)
            if atual == self.raiz:
                self.raiz = sucessor
            else:
                if filho_esquerda:
                    pai.esquerda = sucessor
                else:
                    pai.direita = sucessor
            sucessor.esquerda = atual.esquerda

        return True

    def print_Arvore(self, metodo):

        if metodo == "preOrder":
            return print(self.preOrder(self.raiz,""))

        elif metodo == "inOrder":
            return print(self.inOrder(self.raiz,""))

        elif metodo == "postOrder":
            return print(self.postOrder(self.raiz,""))




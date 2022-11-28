from node import Node

class BinaryTree:

    def __init__(self):
        self.root = Node(None, None, None)
        self.root = None

    def adicionar(self, valor):
        novo = Node(valor, None, None)
        if self.root == None:
            self.root = novo
        else:
            atual = self.root
            while True:
                anterior = atual
                if valor <= atual.item:
                    atual = atual.esquerda
                    if atual == None:
                        anterior.esquerda = novo
                        return

                else:
                    atual = atual.direita
                    if atual == None:
                        anterior.direita = novo
                        return


    def remover(self, valor):
        if self.root == None:
            return False
        atual = self.root
        pai = self.root
        filho_esquerda = True

        while atual.item != valor:
            pai = atual
            if valor < atual.item:
                atual = atual.esq
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
            sucessor = self.noSucessor(atual)

            if atual == self.root:
                self.root = sucessor
            else:
                if filho_esquerda:
                    pai.esq = sucessor
                else:
                    pai.dir = sucessor
            sucessor.esq = atual.esq

        return True

    def noSucessor(self, apaga):
        paidoSucessor = apaga
        Sucessor = apaga
        atual = apaga.direita

        while atual != None:
            paidoSucessor = Sucessor
            Sucessor = atual
            atual = atual.esquerda

        if Sucessor != apaga.direita:
            paidoSucessor.esq = Sucessor.direita
            Sucessor.direita = apaga.direita
        return Sucessor

    def inOrder(self, atual):
        if atual != None:
            self.inOrder(atual.esquerda)
            print(atual.item, end=" ")
            self.inOrder(atual.direita)

    def preOrder(self, atual):
        if atual != None:
            print(atual.item, end=" ")
            self.preOrder(atual.esquerda)
            self.preOrder(atual.eita)

    def posOrder(self, atual):
        if atual != None:
            self.posOrder(atual.esquerda)
            self.posOrder(atual.direita)
            print(atual.item, end=" ")

    def height(self, atual):
        if atual == None or atual.esquerda == None and atual.direita == None:
            return 0
        else:
            if self.height(atual.esquerda) > self.height(atual.direita):
                return 1 + self.height(atual.esquerda)
            else:
                return 1 + self.height(atual.direita)

    def folhas(self, atual):
        if atual == None:
            return 0
        if atual.esq == None and atual.dir == None:
            return 1
        return self.folhas(atual.esq) + self.folhas(atual.dir)

    def contarNos(self, atual):
        if atual == None:
            return 0
        else:
            return 1 + self.contarNos(atual.esquerda) + self.contarNos(atual.direita)


    def caminhar(self):
        print(" Printando em Ordem: ", end="")
        self.inOrder(self.root)
        print("\n Printando em Pos-Ordem: ", end="")
        self.posOrder(self.root)
        print("\n Printando em Pre-Ordem: ", end="")
        self.preOrder(self.root)
        print("\n Altura: " % (self.height(self.root)))
        print("  folhas: " % (self.folhas(self.root)))
        print("  Nós: " % (self.contarNos(self.root)))

class Node:
    def __init__(self, valor, direita = None, esquerda = None):
        self.esquerda = esquerda
        self.direita = direita
        self.valor = valor

    def setDireita(self, direita):
            self.direita = direita

    def setEsquerda(self, esquerda):
            self.esquerda = esquerda


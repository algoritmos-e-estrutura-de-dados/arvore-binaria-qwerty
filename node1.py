class Node:
    def init(self, val, direita = None, esquerda = None):
        self.esquerda = esquerda
        self.direita = direita
        self.valor = val

    def setDireita(self, direita):
            self.direita = direita

    def setEsquerda(self, esquerda):
            self.esquerda = esquerda

    def getDireita(self):
        return self.direita

    def getEsquerda(self):
        return self.esquerda

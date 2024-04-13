import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    #O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O Vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, '-', self.valores[i])

    #0(2)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        
        self.ultima_posicao += 1
        self.valores[self.ultima_posicao] = valor
    
    #O(n)
    def pesquisar(self, valor):
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        
        return -1
    
    #O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)

        if posicao == -1:
            return -1
        
        for i in range(posicao, self.ultima_posicao):
            self.valores[i] = self.valores[i+1]

        self.ultima_posicao -= 1
        
vetor = VetorNaoOrdenado(10)
vetor.imprime()

vetor.insere(1)
vetor.imprime()
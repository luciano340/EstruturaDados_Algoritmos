import numpy as np

class VetorOrdenado:
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
    
    #0(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        
        p = 0
        for i in range(self.ultima_posicao + 1):
            p = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                p = i + 1
            
        x = self.ultima_posicao
        while x >= p:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        
        self.valores[p] = valor
        self.ultima_posicao += 1

    #O(n)     
    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                print(-1)
                return -1
            if self.valores[i] == valor:
                print(i)
                return i 

        print(-1)       
        return -1
    
    #O(log n)
    def pesquisa_binaria(self,valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = int((limite_inferior + limite_superior) / 2)

            if self.valores[posicao_atual] == valor:
                return posicao_atual
            
            elif limite_inferior > limite_superior:
                return -1
            
            else:
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_superior = posicao_atual - 1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        
        for i in range(posicao, self.ultima_posicao):
            self.valores[i] = self.valores[i + 1]
        
        self.ultima_posicao -= 1
        
a = VetorOrdenado(10)

a.insere(10)
a.insere(2)
a.insere(5)
a.insere(22)
a.insere(8)
a.imprime()

a.excluir(8)
print('\n')
a.imprime()

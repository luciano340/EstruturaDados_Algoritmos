import numpy as np

class Pilha:

    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.self.__capacidade, dytpe=int)
    
    def __verificar_pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        return False
    
    def __verificar_pilha_vazia(self):
        if self.__topo == -1:
            return True
        return False
    
    def empilhar(self, valor):
        if self.__verificar_pilha_cheia:
            print('A pilha está cheia')
            return None
        
        self.__topo += 1
        self.__valores[self.__topo] = valor
    
    def desempilhar(self):
        if self.__verificar_pilha_vazia:
            print('Está vázia')
            return None
        
        self.__topo -= 1
    
    def ver_topo(self):
        if self.__topo != -1:
            return self.__valore[self.__topo]
        return False
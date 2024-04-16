import numpy as np 

class ValidadorExpressoes:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.validadores_abertura = ['(', '[', '{']
        self.validadores_fechamento = [')', ']', '}']
        self.__ProximoValidador = None
        self.__valores = np.empty(self.__capacidade, dtype=str)
        self.__topo = -1
            
    def validar(self, expressao):

        for i in expressao:
            self.__imprimir()
            if i in self.validadores_abertura:
                self.__empilhar(i)
            elif i in self.validadores_fechamento:
                if not self.__verificar_pilha_vazia():
                    ch = str(self.__desempilhar())
                    if (i == '}' and ch != '{') or (i == ']' and ch != '[') or (i == ')' and ch != '('):
                        print(f'Erro: {ch} na posição {i}')
                        self.__limpar_pilha()
                        break
                else:
                    print(f'Erro: {i}')
                    break

            
    def __verificar_pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        return False
    
    def __verificar_pilha_vazia(self):
        if self.__topo == -1:
            return True
        return False
    
    def __empilhar(self, valor):
        if self.__verificar_pilha_cheia():
            print('A pilha está cheia')
            return None
           
        self.__topo += 1
        self.__valores[self.__topo] = valor
    
    def __desempilhar(self):
        if self.__verificar_pilha_vazia():
            print('Está vázia')
            return None
        
        valor = self.__valores[self.__topo]
        self.__topo -= 1
        return valor
    
    def __limpar_pilha(self):
        self.__topo = -1
    
    def __imprimir(self):
        if self.__topo == -1:
            print('Pilha vazia')
            return None
        
        for i in range(self.__topo +1):
            print(f'{i} - {self.__valores[i]}')

a = ValidadorExpressoes(10)
a.validar("2+2]")
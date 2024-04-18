import numpy as np

class No:
    def __init__(self, valor):
        self.__valor = valor
        self.__proximo = None
    
    def mostra_no(self):
        print(self.__valor)
    
    def get_valor(self):
        return self.__valor
    
    def set_proximo(self, proximo):
        self.__proximo = proximo
    
    def get_proximo(self):
        return self.__proximo
    
class ListaEncadeada:
    def __init__(self):
        self.__primeiro = None
    
    def insere_inicio(self, valor):
        novo = No(valor)
        novo.set_proximo(self.__primeiro)
        self.__primeiro = novo

    def mostrar(self):
        if self.__primeiro == None:
            print('Lista Vazia!')
            return None
        
        atual = self.__primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.get_proximo()
    
    def excluir_primeiro(self):
        temp = self.__primeiro
        if self.__primeiro.get_proximo() == None:
            return None
        self.__primeiro = self.__primeiro.get_proximo()

    def pesquisa(self, valor):
        if self.__primeiro == None:
            print('Lista Vazia!')
            return None
        
        atual = self.__primeiro
        while atual != None:
            valor_atual = atual.get_valor()
            if valor_atual == valor:
                print(f'Localizado {valor_atual} - {atual}')
                return atual
            atual = atual.get_proximo()
        print(f'Não foi possível localizar o valor {valor}!')
        return None

    def excluir_valor(self, valor):
        atual = self.__primeiro
        anterior = self.__primeiro

        while atual.get_valor() != valor:
            if atual.get_proximo() == None:
                return None
            anterior = atual
            atual = atual.get_proximo()
        
        if atual == self.__primeiro:
            self.__primeiro = self.__primeiro.get_proximo()
        else:
            anterior.set_proximo(atual.get_proximo())
        return atual
    
lista = ListaEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(22)
lista.insere_inicio(42)
lista.mostrar()
lista.excluir_primeiro()
print('\n')
lista.mostrar()
print('\n')
lista.pesquisa(58)
lista.pesquisa(1)
print('\n')
lista.insere_inicio(72)
lista.insere_inicio(55)
lista.insere_inicio(122)
lista.insere_inicio(189)
lista.mostrar()
print('\n')
lista.excluir_valor(122)
lista.mostrar()
import numpy as np

class No:
    def __init__(self, valor):
        self.__valor    = valor
        self.__proximo  = None
        self.__anterior = None
    
    def mostra_no(self):
        print(self.__valor)
    
    def get_valor(self):
        return self.__valor
    
    def set_proximo(self, proximo):
        self.__proximo = proximo
    
    def get_proximo(self):
        return self.__proximo

    def get_anterior(self):
        return self.__anterior

    def set_anterior(self, valor):
        self.__anterior = valor
    
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo   = None
    
    def __lista_vazia(self):
        return self.__primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.__ultimo = novo
        else:
            self.__primeiro.set_anterior(novo)
        
        novo.set_proximo(self.__primeiro)
        self.__primeiro = novo
    
    def insere_final(self, valor):
        novo = No(valor)
        if self.__lista_vazia():
            self.__primeiro = novo
        else:
            self.__ultimo.set_proximo(novo)
            novo.set_anterior(self.__ultimo)
        self.__ultimo = novo
    
    def mostrar_frente(self):
        atual = self.__primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.get_proximo()
        
    def mostrar_tras(self):
        atual = self.__ultimo
        while atual != None:
            atual.mostra_no()
            atual = atual.get_anterior()
    
    def excluir_inicio(self):
        temp = self.__primeiro
        if self.__primeiro.get_proximo() == None:
            self.__ultimo = None
        else:
            self.__primeiro.get_proximo().set_anterior(None)
        
        self.__primeiro = self.__primeiro.get_proximo()
        return temp

    def excluir_final(self):
        temp = self.__ultimo
        if self.__primeiro.set_proximo(None):
            self.__primeiro = None
        else:
            self.__ultimo.get_anterior().set_proximo(None)
        self.__ultimo = self.__ultimo.get_anterior()
        return temp

    def excluir_valor(self, valor):
        atual = self.__primeiro
        while atual.get_valor() != valor:
            atual = atual.get_proximo()
            if atual == None:
                return None
        if atual == self.__primeiro:
            self.__primeiro = atual.get_proximo()
        else:
            atual.get_anterior().set_proximo(atual.get_proximo())

        if atual == self.__ultimo:
            self.__ultimo = atual.get_anterior()
        else:
            atual.get_proximo().set_anterior(atual.get_anterior())
        return atual
        

lista = ListaDuplamenteEncadeada()
lista.insere_inicio(1)
lista.insere_inicio(10)
lista.mostrar_tras()
lista.mostrar_frente()
print('\n')
lista.insere_final(222)
lista.mostrar_frente()
lista.excluir_inicio()
print('\n')
lista.mostrar_frente()
lista.excluir_final()
print('\n')
lista.mostrar_frente()
lista.insere_inicio(520)
lista.insere_final(1024)
lista.insere_final(2015)
print('\n')
lista.mostrar_frente()
lista.excluir_valor(1024)
print('\n')
lista.mostrar_frente()

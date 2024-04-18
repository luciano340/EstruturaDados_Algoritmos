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

class ListaEncadeadaExtremidadaDupla:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
    
    def __lista_vazia(self):
        return self.__primeiro == None

    def insere_inicio(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            self.__ultimo = novo
        novo.set_proximo(self.__primeiro)
        self.__primeiro = novo
    
    def insere_final(self, valor):
        novo = No(valor)

        if self.__lista_vazia():
            self.__primeiro = novo
        self.__ultimo.set_proximo(novo)
        self.__ultimo = novo
    
    def mostrar(self):
        if self.__lista_vazia():
            print('Lista Vazia!')
            return
        atual = self.__primeiro
        while atual != None:
            atual.mostra_no()
            atual = atual.get_proximo()
    
    def excluir_inicio(self):
        if self.__lista_vazia():
            print('Lista vazia!')
            return
        temp = self.__primeiro

        if self.__primeiro.get_proximo() == None:
            self.__ultimo = None
        self.__primeiro = self.__primeiro.get_proximo()
        return temp

lista = ListaEncadeadaExtremidadaDupla()
lista.insere_inicio(1)
lista.insere_inicio(22)
lista.mostrar()
print('\n')
lista.insere_final(100)
lista.mostrar()
print('\n')
lista.excluir_inicio()
lista.mostrar()


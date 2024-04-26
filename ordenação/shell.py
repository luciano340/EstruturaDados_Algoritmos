import numpy as np
from random import randint

def shell_sort(vetor):
    intervalo = len(vetor)//3

    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            
            vetor[j] = temp
        intervalo //= 2
    return vetor


array = np.array([randint(0,50000) for _ in range(50)] )
print(f'\nArray não ordando {array}')
a = shell_sort(array)
print(f'\nArray ordenado: {a}')
import numpy as np
from random import randint

def selection_sort(vetor):
    n = len(vetor)

    for i in range(n):
        id_min = i
        for j in range(i + 1 , n):
            if vetor[id_min] > vetor[j]:
                id_min = j
        temp = vetor[i]
        vetor[i] = vetor[id_min]
        vetor[id_min] = temp

    return vetor
array = np.array([randint(0,5000) for _ in range(50)] )
print(f'\nArray não ordando {array}')
a = selection_sort(array)
print(f'\nArray ordenado: {a}')
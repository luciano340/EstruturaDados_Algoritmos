import numpy as np
from random import randint

def bubble_sort(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range(0, n - i  - 1):
            if vetor[j] > vetor[j+1]:
                temp = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = temp
    
    return vetor

array = np.array([randint(0,5000) for _ in range(50)] )
print(f'\nArray não ordando {array}')
a = bubble_sort(array)
print(f'\nArray ordenado: {a}')
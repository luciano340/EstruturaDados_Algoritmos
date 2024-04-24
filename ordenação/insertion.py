import numpy as np
from random import randint

def insertion_sort(vetor):
    n = len(vetor)

    for i in range(1, n):
        marcado = vetor[i]
        j = i - 1

        while j >= 0 and marcado < vetor[j]:
            vetor[ j + 1 ] = vetor[j]
            j -= 1
        vetor[j+1] = marcado
    return vetor

array = np.array([randint(0,5000) for _ in range(50)] )

print(f'\nArray não ordando {array}')
a = insertion_sort(array)
print(f'\nArray ordenado: {a}')
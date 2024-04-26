import numpy as np
from random import randint

def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio - 1

    for j in range(inicio, final):
        if vetor[j] <= pivo: 
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
        
    vetor[i + 1], vetor[final] = vetor[final], vetor[i + 1]
    return i + 1

def quick_sort(vetor, inicio, final):
    if inicio < final:
        posicao = particao(vetor, inicio, final)
        quick_sort(vetor, posicao  + 1, posicao - 1)
        quick_sort(vetor, posicao + 1, final)
    return vetor

array = np.array([randint(0,50000) for _ in range(50)] )
print(f'\nArray não ordando {array}')
a = quick_sort(array, 0, len(array) - 1)
print(f'\nArray ordenado: {a}')
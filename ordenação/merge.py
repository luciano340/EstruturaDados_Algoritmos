import numpy as np
from random import randint

def merge_sort(vetor):
  if len(vetor) > 1:
    divisao = len(vetor) // 2
    esquerda = vetor[:divisao].copy()
    direita = vetor[divisao:].copy()

    merge_sort(esquerda)
    merge_sort(direita)

    i = j = k = 0

    # Ordena esquerda e direita
    while i < len(esquerda) and j < len(direita):
      if esquerda[i] < direita[j]:
        vetor[k] = esquerda[i]
        i += 1
      else:
        vetor[k] = direita[j]
        j += 1
      k += 1

    # Ordenação final
    while i < len(esquerda):
      vetor[k] = esquerda[i]
      i += 1
      k += 1
    while j < len(direita):
      vetor[k] = direita[j]
      j += 1
      k += 1
  return vetor

array = np.array([randint(0,50000) for _ in range(50)] )
print(f'\nArray não ordando {array}')
a = merge_sort(array)
print(f'\nArray ordenado: {a}')
import timeit

#o(n)
def func1(n):
    numb = 0
    for i in range(n + 1):
        numb += 1
    
    return numb

#o(3)
def func2(n):
    return (n * (n +1)) /2

a = timeit.timeit('func1(1000)', 'from __main__ import func1', number=10000)
b = timeit.timeit('func2(1000)', 'from __main__ import func2', number=10000)

print(f'Tempo gasto func1\t{a}\ntempo gasto func2\t{b}')

def func3():
    lista = []
    for i in range(1000):
        lista += [i]
    
    return lista

def func4():
    return range(1000)

c = timeit.timeit('func3()', 'from __main__ import func3', number=10000)
d = timeit.timeit('func4()', 'from __main__ import func4', number=10000)
print(f'Tempo gasto func3\t{c}\ntempo gasto func4\t{d}')
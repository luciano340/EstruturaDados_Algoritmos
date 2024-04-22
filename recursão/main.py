#A função retorna ela mesma sem fim
def recursao():
    print('Recursão')
    return recursao()

#Recursão com limite
def recursao2(i):
    print(f'Recursão {i}')
    i += 1
    if i >= 5:
        return None
    return recursao2(i)

#função com loop convencional
def soma(n):
    soma = 0
    for i in range(n + 1):
        soma += i
    return soma

r = soma(5) #deve retornar 15
print(r)

#função utilizando recursão
def soma2(n):
    if n == 0:
        return 0

    return n + soma2(n - 1)

r = soma2(5) #deve retornar 15
print(r)
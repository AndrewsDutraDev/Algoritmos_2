def soma_elementos(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[-1] + soma_elementos(lista[:-1])

def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def fibonacci(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def soma_digitos(n):
    if n <= 9:
        return n
    else:
        resto = n%10
        n = n//10
        return resto + soma_digitos(n)

    


# print(soma_elementos([1, 2, 3,10]))

# print(fatorial(1))
# print(fatorial(2))
# print(fatorial(3))
# print(fatorial(4))
# print(fatorial(5))

# print(fibonacci(6))

# print(soma_digitos(14))


print(soma_digitos(14))

#Feito por Andrews, Guilherme e Mateus.

#1- Soma dos elementos de uma lista:
def soma_elementos(lista):
    soma = 0
    for elem in lista:
        soma = soma + elem
    return soma

#2- Fatorial de um determinado número
def fatorial(n):
    total = n 
    while n > 1:
        total = total * (n-1)
        n = n-1
    return total

#3- Fibonacci de um determinado número: 
def fibonacci(N):
    vetor = [0, 1]
    if N > 1:
       for i in range(2, N+1):
           func = vetor[i - 1] + vetor[i - 2]
           vetor.append(func)
    # print( vetor)
    return vetor[N]

#4- Soma dos dígitos de um número inteiro
def soma_digitos(n):
    if n <= 9:
        return n
    soma = 0
    while n > 9:
        resto = n%10
        n = n//10
        soma = soma + resto
    return soma + n   


# print(soma_elementos([1, 2, 3,10]))

# print(fatorial(1))
# print(fatorial(2))
# print(fatorial(3))
# print(fatorial(4))
# print(fatorial(5))

# print(fibonacci(6))

# print(soma_digitos(14))

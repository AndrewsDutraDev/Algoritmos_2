lista_auxiliar = ['a','b','c',None]
lista = [None, None, None]
tamanho = 3
posicao = 0

for x in range(0, posicao):
    lista[x] = lista_auxiliar[x]
for x in range(posicao , tamanho):
    lista[x] = lista_auxiliar[x + 1]

print(lista)
lista_auxiliar = ['a','b','c','d', None]
lista = [None, None, None, None, None, None]
tamanho = 6
posicao = 4
produto = 'F'

produto_adicionado = False
for x in range(0, tamanho):
    if (x + 1) == posicao:
        lista[x] = produto
        produto_adicionado = True
    else:
        if produto_adicionado == True:
            lista[x] = lista_auxiliar[x - 1]
        else:
            lista[x] = lista_auxiliar[x] 

print(lista)
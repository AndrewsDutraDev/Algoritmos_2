lista = [('Abobora', '21/05/2019', '-->'), ('Abacate', '12/11/1999', '-->'), ('Maça', '07/04/2012', '-->')]
aux = 0
nonva_lista = [None, None, None]
for x in range(len(lista), 0, -1):
    nonva_lista[aux] = lista[x]
    aux+=1

print(lista)
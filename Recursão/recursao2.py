# Busca Encadeada Recursiva
def busca_encadeada():
    if (len(lista) == 0):
        return
    else:
        if (lista[0] == produto):
            return cont
        else:
            cont = cont + 1
            return busca_encadeada(lista[1:], produto, cont)

# Busca Linear Recursiva
def busca_linear_recursiva(lista, produto, cont):
    if (len(lista) == 0):
        return
    else:
        if (lista[0] == produto):
            return cont
        else:
            cont = cont + 1
            return busca_linear_recursiva(lista[1:], produto, cont)

# Ordenação para busca binária em tabela
def ordena(lista2):
    cont = 1
    for i in range(len(lista2) - 1, 0, -1):
        for j in range(i):
            if lista2[j] > lista2[j + 1]:
                (lista2[j], lista2[j + 1]) = (lista2[j + 1], lista2[j])
    return lista2

#Função que executa os dois tipos de listas
def busca(lista, tipo, produto):
    if (tipo == 'bin'):
        listaOrd = ordena(lista)
        return busca_linear_recursiva(listaOrd, produto, cont)
    else:
        return busca_linear_recursiva(lista, produto, cont)

#Função de busca binária
def search_bin(lista, produto, inicio, fim): #função para buscar de forma binária
    if len(lista):
        mid = ((inicio + fim) // 2)
        if lista[mid] == produto:
            return mid + 1
        if (produto < lista[mid]):
            return self.search_bin(lista, produto, inicio, mid - 1)
        else:
            return self.search_bin(lista, produto, mid + 1, fim)
    return



cont = 1
lista = [5,3,1,2,8]
tipo = 'lin'
produto = 2
print(busca(lista, tipo, produto))
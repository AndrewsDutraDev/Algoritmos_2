from TAD_ContiguidadeFisica import Pilha
from TAD_Encadeamento import PilhaEnc

print('Digite 1 - contiguidade , 2- encadeamento')
type_list = int(input('Digite o tipo de lista desejado:'))
iniciar = True
if(type_list == 1 ):
    tam =(int(input('Qual o tamanho da sua pilha? ')))
    lista = Pilha(tam)
else:
    lista = PilhaEnc()
while iniciar:
    #print('\nLista atualizada: ',lista.get_list())
    print('0 - Sair do programa')
    print('1 - Inserir nó do topo da pilha.')
    print('2 - Remover nó do topo da pilha.')
    print('3 - Consultar nó do topo da pilha')
    print('4 - Destruir pilha')
    operation = int(input('Qual operação deseja realizar? '))
    if (operation == 0):
        iniciar = False
    if (operation == 1):
        value = input("Qual o valor do nó: ")
        lista.insert_top(value)
    if (operation == 2):
        lista.remove_top()
    if (operation == 3):
        print("O conteúdo do topo é: "+str(lista.query()))
    if (operation == 4):
        lista.destroy()
    if (operation == 5):
        print('Você está na segunda lista')
        if (type_list == 1): 
            times = int(input('Quantos valores você quer na lista secundária? '))
            lista_sec = Pilha(times)
            for i in range(0, times):
                value = input("Qual é o "+ str(i+1) +"° valor da lista: ")
                lista_sec.insert_top(value)
            print("As listas são iguais? "+str(lista.compare(lista.get_list(), lista_sec.get_list())))
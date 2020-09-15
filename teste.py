# Feito em conjunto por: Andrews Dutra, Mateus Marques e Guilherme Steglich
class Product:
    def __init__(self,name):
        self.name = name

class List:
    def __init__(self, size):
        self.list = [None]*size

    def put_list(self,position,product):
        count_size = 0
        for size_list in self.list:
            count_size = count_size + 1
        # print (count_size)
        # print(self.list)
        for element in range(0,count_size,-1): 
            if (self.list[element] == None):           
                aux_index_element = element
                print('auxiliar'+str(aux_index_element))
            
            
            




            # if self.list[element] == None:
            #     aux_index_element = element
            #     if aux_index_element > position:
            #         for last_list in range(position-1, count_size,-1):
            #             self.list[last_list] = self.list[last_list-1]
            #             print(self.list)
            #         if (self.list[position-1] == None):
            #             self.list[position-1] = product
            #         else:
            #             for last_list in range(position-1, count_size,-1):
            #                 self.list[last_list] = self.list[last_list-1]
                # elif aux_index_element < position:
                    



                


                

                    

                
        # [none,a,C,b]


list = List(int(input('Qual o tamanho da sua lista? ')))
iniciar = True
while iniciar:
    # print('Lista atualizada: ',list.exibirlista())
    print('0 - Sair do programa')
    print('1 - Inserir produto a lista.')
    print('2 - Remover produto da lista.')
    print('3 - Localizar produto na lista.')
    print('4 - Limpar lista.')
    operacao = int(input('Qual operação deseja realizar? '))
    if (operacao == 0):
        iniciar = False
    if (operacao == 1):
        product = Product(input("Qual o nome do produto: "))
        list.put_list(int(input("Digite a posição do produto: ")),product.name)
    # if (operacao == 2):
    #     posicao = int(input("Digite a posição do produto que você quer remover: "))
    #     lista.removerproduto(posicao)
    # if (operacao == 3):
    #     produto = input("Digite o nome do produto que você quer encontrar: ")
    #     print("O produto está na posição: "+str(lista.posicaoproduto(produto)))
    # if (operacao == 4):
    #     lista.limparlista()
class Product:
    def __init__(self,name):
        self.name = name

class List:
    def __init__(self,size):
        self.size = size
        self.list = [None]*size

    def put_list(self,position,product):
        count_times = 0
        count_none = 0
        for element in range(0,self.size):
            if (self.list[element] == None): 
                print('element: '+str(element))
                count_none = count_none + 1
                print('count: '+str(count_none))
                position_none = element
        for element_list in range(0,position-1):
            # print('range: '+str(element_list))
            # print('self.list: '+str(self.list[element_list]))
            if self.list[element_list] == None:
                # print('element list '+str(element_list))
                # print('position '+str(position))                
                # print('veio aqui')                    
                if (count_times == 0):
                    self.list[element_list] = product
                count_times = count_times + 1
                # funcionando ate aqui
            elif (self.list[element_list] != None):
                print('ta caindo aqui')
                for last_list in self.list[position::-1]:
                    print('last list: '+str(last_list))
                    print('last SELF list: '+str(self.list[last_list]))
                    self.list[last_list] = self.list[last_list-1]
                #self.list[position] = product
            


                # if (count_none != self.size):
                    # if (position > position_none):
                    #     self.list[position_none] = product     

                    # if (position < position_none):
                    #     if (self.list[position] != None):
                    #         for last_list in range(position-1, self.size,-1):
                    #             self.list[last_list] = self.list[last_list-1]
                            


                # elif (position_none == position):
                #     self.list[element-1] = product
                # elif (position_none > position):                    
                #     for last_list in range(position-1, self.size,-1):                        
                #         self.list[last_list] = self.list[last_list-1]
                        
                #for da ultima posição que nao tem none, fazendo a subtraçao disso com o position desejado, se >= 1, o product vai pra ultima posição do != none + 1
        print(self.list)
    # [none,a,none,none]

lista = List(int(input('Qual o tamanho da sua lista? ')))
iniciar = True
while iniciar:
    # print('Lista atualizada: ',lista.exibirlista())
    print('0 - Sair do programa')
    print('1 - Inserir produto a lista.')
    print('2 - Remover produto da lista.')
    print('3 - Localizar produto na lista.')
    print('4 - Limpar lista.')
    operacao = int(input('Qual operação deseja realizar? '))
    if (operacao == 0):
        iniciar = False
    if (operacao == 1):
        produto = Product(input("Qual o nome do produto: "))
        lista.put_list(int(input("Digite a posição do produto: ")),produto.name)
    # if (operacao == 2):
    #     posicao = int(input("Digite a posição do produto que você quer remover: "))
    #     lista.removerproduto(posicao)
    # if (operacao == 3):
    #     produto = input("Digite o nome do produto que você quer encontrar: ")
    #     print("O produto está na posição: "+str(lista.posicaoproduto(produto)))
    # if (operacao == 4):
    #     lista.limparlista()






class Product:
    def __init__(self,name):
        self.name = name

class List:
    def __init__(self,size):
        self.size = size
        self.list = [None]*size

    def put_list(self,position,product):
        count_none = 0
        for num_nones in range(0, self.size):
            if self.list[num_nones] == None:
                count_none += 1
        for element in range(0, self.size):
            print("elemento: "+str(element))
            print("quantidade de none: "+str(count_none))
            if ((self.list[element] == None) and (element < position)): 
                print("primeiro")
                self.list[element] = product
                break
            elif (self.list[element] != None and (element == position-1)):
                print("segundo")
                if (count_none >= 1):
                    for last_element in range(self.size-1, 0, -1 ):
                        print("último elemento: "+str(self.list[last_element]))
                        self.list[last_element] = self.list[(last_element)-1]
                    self.list[position-1] = product
                else:
                    print("Não há espaço suficiente no vetor")
        print(self.list)

    def remove(self, position):
        for element in range(0, self.size):
            if (element == position-1):
                self.list[element] = None
        print(self.list)











lista = List(int(input('Qual o tamanho da sua lista? ')))
iniciar = True
while iniciar:
    # print('Lista atualizada: ',lista.exibirlista())
    print('0 - Sair do programa')
    print('1 - Inserir produto a lista.')
    print('2 - Remover produto da lista.')
    print('3 - Localizar produto na lista.')
    print('4 - Limpar lista.')
    operation = int(input('Qual operação deseja realizar? '))
    if (operation == 0):
        iniciar = False
    if (operation == 1):
        product = Product(input("Qual o nome do produto: "))
        lista.put_list(int(input("Digite a posição do produto: ")),product.name)
    if (operation == 2):
        pos = int(input("Digite a posição do produto que você quer remover: "))
        lista.remove(pos)
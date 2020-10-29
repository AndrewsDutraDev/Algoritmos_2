class Pilha:
    def __init__(self, size):
        self.list = [None] * size
        self.limit = size - 1
        self.base = 0
        self.topo = self.base - 1

    def insert_top(self, value): 
        if (self.topo < self.limit):
            self.topo += 1
            self.list[self.topo] = value
    
    def remove_top(self):
        if (self.topo >= self.base):
            self.topo -= 1
    
    def query(self):
        if (self.topo >= self.base):
            return self.list[self.topo]    
               
    def destroy(self):
        self.topo = self.base - 1

pilha = Pilha(int(input('Qual o tamanho da sua pilha? ')))
iniciar = True
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
        pilha.insert_top(value)
    if (operation == 2):
        pilha.remove_top()
    if (operation == 3):
        print("O conteúdo do topo é: "+str(pilha.query()))
    if (operation == 4):
        pilha.destroy()

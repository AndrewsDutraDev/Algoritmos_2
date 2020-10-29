from config import Nodo

class PilhaEnc:
    def __init__(self):
        self.topo = None
    
    def vazia(self):
        boolean = True
        if (self.topo != None):
            boolean = False
        return boolean

    def insert_top(self, value):
        new = Nodo(value)
        if (not self.vazia()):
            new.next = self.topo
        self.topo = new
    
    def remove_top(self):
        if (not self.vazia()):
            aux = self.topo
            self.topo = aux.next
            del aux

    def query(self):
        if (not self.vazia()):
            return self.topo.value
            
    def destroy(self):
        while (not self.vazia()):
            self.remove_top()

PilhaEnc = PilhaEnc()
iniciar = True
while iniciar:
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
        print(PilhaEnc.insert_top(value))
    if (operation == 2):
        PilhaEnc.remove_top()
    if (operation == 3):
        print("O conteúdo do topo é: "+str(PilhaEnc.query()))
    if (operation == 4):
        PilhaEnc.destroy()

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

    
        


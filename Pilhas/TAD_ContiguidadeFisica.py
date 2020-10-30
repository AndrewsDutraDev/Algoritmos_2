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
    
    def get_list(self):
        return self.list
    
    def cont(self, listAux):
        contList = 0
        for i in listAux:
            contList += 1
        return contList

    def compare(self, list_one, list_two):
        contOne = self.cont(list_one)
        contTwo = self.cont(list_two)
        equallity = True
        if contOne != contTwo:
            equallity = False
        else:
            while contOne >= 0:
                if list_one[contOne-1] == list_two[contOne-1]:
                    contOne -= 1
                else:
                    equallity = False
                    break
        return equallity




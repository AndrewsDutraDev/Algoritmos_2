# Trabalho feito em conjunto por Andrews Dutra, Guilherme Steglich e Mateus Marques 

class Start_list:
    def __init__(self):
        self.start = None

class Features:
    def __init__(self):
        self.list = []
        
    def size_list(self):
        self.count = 0
        for element in self.list:
            self.count += 1
        return self.count

    def insert(self, position, value):
        position = 1
        value = "assistente"
        size = self.size_list()
        if size == 0:
            if position == 1:
                aux = {value: None}
                self.list[0] = aux
        print (self.list )
        # first = self.list[0]

    def destroy(self):
       self.list = []





family = Features()
family.insert(1, "assistente")

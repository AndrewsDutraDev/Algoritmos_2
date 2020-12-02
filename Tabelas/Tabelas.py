class Table:
    def __init__(self, maxSize):
        self.key = [None]*(maxSize+1)
        self.value = [None]*(maxSize+1)
        self.start_limit = 1
        self.end_limit = maxSize
        self.start = self.start_limit - 1
        self.end = self.end_limit + 1
    
    def __repr__(self):
        string = ""
        if (not self.empty()):
            for i in range(self.start, self.end+1)
            string = string + str(self.key[i]) + ": " +str(self.value[i]) + "\n"
        return string + "\n"
    
    ###verifica se está vazia###
    def empty(self):
        return self.start < self.start_limit and self.end > self.end_limit
    
    ##verifica se está cheia###
    def full(self):
        return (self.start == self.start_limit and self.end == self.end_limit)
    
    ###verifica o tamanho da tabela###
    def size(self):
        if not self.empty():
            return self.end - self.start + 1
        else:
            return 0

    ######### O método Search deve chamar o método busca linear ou busca binária. Esses dois métodos devem ser criados

    def search(self, search_key):
        if not self.empty():
            for i in range(self.start, self.end + 1):
                if self.key[i] == search_key:
                    return i
        return 0

    ######### Além do método insert, deve ter o Insert ordenado para que a lista fique ordenada         
    def insert(self, insert_key, insert_value):
        position = self.search(insert_key)
        if (position > 0):
            self.key[position] = insert_key
            self.value[position] = insert_value
        elif (not self.full()):
            if (self.empty()):
                self.start = self.start_limit
                self.end = self.start_limit
            else:
                self.end += 1
            self.key[self.end] = insert_key
            self.value[self.end] = insert_value
                
    def consult(self, search_key):
        position = self.search(search_key)
        if position > 0:
            self.value[position]
        

    def delete(self, delete_key):
        position = self.search(delete_key)
        if (position > 0):
            for i in range(position, self.end):
                self.key[i] = self.key[i+1]
                self.value[i] = self.value[i+1]
            self.end -= 1

    ### destroi toda a tabela ###
    def destroy(self):
        self.start = self.start_limit - 1
        self.end = self.end_limit + 1
        
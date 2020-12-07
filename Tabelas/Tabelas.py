class Table:
    def __init__(self, maxSize):
        self.key = [None]*(maxSize)
        self.value = [None]*(maxSize)
        self.start_limit = 1
        self.end_limit = maxSize
        self.start = self.start_limit - 1
        self.end = self.end_limit + 1
    
    def __repr__(self):
        string = ""
        if (not self.empty()):
            for i in range(self.start-1, self.end):
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

    ######### O método Search deve chamar o método busca linear ou busca binária. ####
    def search(self, target, search_key):
        if target == "bin":
            return self.search_bin(search_key)
        return self.search_lin(search_key)
    
    def search_lin(self, search_key): #busca linear
        if not self.empty():
            for i in range(self.start-1, self.end):
                if self.key[i] == search_key:
                    return i+1
        return 0

    def sort(self): #Função para ordenar a tabela 
        if not self.empty():
            for i in range(self.size() - 1, 0, -1):
                for j in range(i):
                    if self.key[j] > self.key[j + 1]:
                        (self.key[j], self.key[j + 1]) = (self.key[j + 1], self.key[j])
                        (self.value[j], self.value[j + 1]) = (self.value[j + 1], self.value[j])
            return self.key

    def search_bin(self, search_key): #função para buscar de forma binária
        if not self.empty():
            self.sort()
            if (self.size() % 2 != 0):
                mid = int((self.size())/2) + 1
            else: 
                mid = int((self.size())/2)
            if (self.key[mid] >= search_key):
                if (self.key[mid] == search_key):
                    return mid+1
                for i in range(0, mid):
                    if (self.key[i] == search_key):
                        return i+1
            else:
                for i in range(mid, self.size()):
                    if (self.key[i] == search_key):
                        return i+1
         
    ######### Além do método insert, deve ter o Insert ordenado para que a lista fique ordenada         
    def insert(self, insert_key, insert_value):
        position = self.search(insert_key, "lin")
        if (position > 0):
            self.key[position] = insert_key
            self.value[position] = insert_value
        elif (not self.full()):
            if (self.empty()):
                self.start = self.start_limit
                self.end = self.start_limit
            else:
                self.end += 1
            self.key[self.end-1] = insert_key
            self.value[self.end-1] = insert_value
    
    def insert_sort(self, insert_key, insert_value): #função que insere de forma ordenada na tabela
        self.insert(insert_key, insert_value) 
        self.sort()

    def consult(self, search_key, target): #função que consulta um valor 
        position = self.search(target, search_key)
        if position > 0:
            self.value[position]
        

    def delete(self, delete_key, target): #função que deleta dado valor da tabela
        position = self.search(target, delete_key)
        if (position > 0):
            for i in range(position-1, self.end-1):
                self.key[i] = self.key[i+1]
                self.value[i] = self.value[i+1]
            self.end -= 1
        return self.__repr__()
    
    ### destroi toda a tabela ###
    def destroy(self):
        self.start = self.start_limit - 1
        self.end = self.end_limit + 1
        
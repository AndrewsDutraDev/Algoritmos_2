class Table:
    def __init__(self, maxSize):
        self.key = [None]*(maxSize)
        self.value = [None]*(maxSize)
        self.start_limit = 1
        self.end_limit = maxSize
        self.start = self.start_limit - 1
        self.end = self.end_limit + 1
    
    #def __repr__(self):
    #    string = ""
    #    if (not self.empty()):
    #        for i in range(self.start, self.end+1):
    #            string = string + str(self.key[i]) + ": " +str(self.value[i]) + "\n"
    #    return string + "\n"
    
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
        if (position >= 0):
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
        if position >= 0:
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
    
    def get(self):
        return self.key


itens = ['marca', 'modelo', 'ano', 'proprietário']
valores = [None]*4
table = Table(int(input('Qual o tamanho da sua Tabela? ')))
iniciar = True
while iniciar:
    print('\nTabela atualizada: ',table.get())
    print('0 - Sair do programa')
    print('1 - Inserir registro a lista.')
    print('2 - Consultar chave.')
    print('')
    print('')
    operation = int(input('Qual operação deseja realizar? '))
    if (operation == 0):
        iniciar = False
    if (operation == 1):
        chave = input("Qual a chave do veículo: ")
        for x in range(0, 4):
            valores[x] = input('Qual '+str(itens[x])+':')
        table.insert(chave, valores)       
    if (operation == 2):
        chave = input("Qual a chave: ")
        print(table.consult(chave))
    if (operation == 3):
        product = input("Digite o nome do produto que você quer encontrar: ")
        print("O produto está na posição: "+str(lista.get_product(product)))
    if (operation == 4):
        lista.clear_list()
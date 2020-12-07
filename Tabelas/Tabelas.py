class Table:
    def __init__(self, tamanho):
        self.chave = [None]*(tamanho)
        self.valor = [None]*(tamanho)
        self.tamanho = tamanho

    def consultar(self, chave):
        cont = 0
        for x in self.chave:
            cont += 1
            if x == chave:
                return 'Os registro da chave ' + self.chave[cont] + ' são: ' + self.valor[cont]
        return 'Registro não encontrado.'

    def inserir(self, posicao, chave, valor):
        if not self.cheia() and not self.busca(chave):
            if self.chave[posicao] == None:
                for x in range(0, self.tamanho):
                    if self.chave[x] == None:
                        self.chave[x] = chave
                        self.valor[x] = valor
                        return
            else:
                for x in range(0, self.tamanho):
                    if x == posicao:
                        for i in range(x, self.tamanho): 
                            self.chave[x + 1] = self.chave[i - 1]
                            self.valor[x + 1] = self.valor[i - 1]
                        self.chave[x] = chave
                        self.valor[x] = valor
                        return
        else:
            return

    def inserir_ordenada(self, chave, valor):
        produto_adicionado = False
        if not self.cheia() and not self.busca(chave):
            if self.vazia():
                self.chave[0] = chave
                self.valor[0] = valor
                return 'Inserido'
            else:
                for x in range(0, self.tamanho):
                    if chave[0] < self.chave[x][0]:
                        for i in range(x, self.tamanho): 
                            self.chave[i] = self.chave[i + 1]
                            self.valor[i] = self.valor[i + 1]
                        self.chave[x] = chave
                        self.valor[x] = valor
                        produto_adicionado = True
                        return 'Inserido'
                    elif chave[0] == self.chave[x][0]:
                        for i in self.chave[x]:
                            if chave[x + 1] < i:
                                for b in range(x, self.tamanho): 
                                    self.chave[b] = self.chave[b + 1]
                                    self.valor[b] = self.valor[b + 1]
                                self.chave[x] = chave
                                self.valor[x] = valor
                                produto_adicionado = True
                                return 'Inserido'
                if not produto_adicionado:
                    for x in range(0, self.tamanho):
                        if x == None:
                            self.chave[x] = chave
                            self.valor[x] = valor  
                            return 'Inserido'
        return 'Não inserido'        

    def remover(self, chave):
        if not self.vazia() and self.busca(chave):
            for x in range(0, self.tamanho):
                if self.chave[x] == chave:
                    self.chave[x] == None
                    for i in range(x, self.tamanho):
                        self.chave[i] = self.chave[i + 1]
                        self.valor[i] = self.valor[i + 1]
                    return 'Removido'
        else:
            return 'Não removido'
    
    def atualizar(self):
        return self.chave

    def destruir(self):
        self.chave = [None] * self.tamanho
        return
    
    def busca(self, chave):
        if not self.vazia():
            for x in self.chave:
                if x == chave:
                    return True
            return False
        else:
            return False

    #def busca_binaria(self, chave):
        #if not self.vazia():
            #m = self.tamanho//2
            #if self.chave[m] == chave:
                #return m
            #elif chave < self.chave[m]:
                #return self.busca_binaria(chave)
            #binario = self.tamanho // 2
            #lista_aux = self.chave
            #while binario != 1:
                #if lista_aux[binario][0] > chave[0]:
                    #for x in range(0, binario):
                        #lista_aux[x] = self.chave[x]
                    #binario = self.tamanho // 2
                        

    #Complementares
    def vazia(self):
        if self.chave[0] == None:
            return True
        else:
            return False

    def cheia(self):
        for x in self.chave:
            if x == None:
                return False
        return True
    
table = Table(int(input('Qual o tamanho da sua Tabela? ')))
itens = ['marca', 'modelo', 'ano', 'proprietário']
iniciar = True
while iniciar:
    print('Tabela atualizada: ',table.atualizar())
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
        posicao = int(input("Qual a posicao: "))
        valores = [None]*4
        for x in range(0, 4):
            valores[x] = input('Qual '+str(itens[x])+':')
        table.inserir(posicao - 1, chave, valores)       

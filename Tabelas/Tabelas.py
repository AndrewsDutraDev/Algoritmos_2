class Table:
    def __init__(self, tamanho):
        self.chave = [None]*(tamanho)
        self.valor = [None]*(tamanho)
        self.tamanho = tamanho
        #self.limite_inicial = 0
        #self.limite_final = tamanho

    def consultar(self, chave):
        cont = 0
        for x in self.chave:
            cont += 1
            if x == chave:
                return 'Os registro da chave ' + self.chave[cont] + ' são: ' + self.valor[cont]
        return 'Vazio'

    def inserir(self, posicao, chave, valor):
        if not self.cheia() and not busca_sequencial(chave):
            if self.pos_vazia(posicao):
                for x in range(0, self.tamanho):
                    if x == None:
                        self.chave[x] = chave
                        self.valor[x] = valor
            else:
                for x in range(0, self.tamanho):
                    if x == posicao:

    #def inserir_ordenada(self):

    def remover(self):
    def destruir(self):
    #def buscar(self):
    def busca_sequencial(self, chave):
        if not self.vazia():
            for x in self.chave:
                if x == chave:
                    return True
            return False
        else:
            return

    def busca_binaria(self):

    #Complementares
    def pos_vazia(self, posicao):
        if self.chave == None:
            return True
        else:
            return False
    
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
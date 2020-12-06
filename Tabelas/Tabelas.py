class Table:
    def __init__(self, tamanho):
        self.chave = [None]*(tamanho)
        self.valor = [None]*tamanho)
        self.limite_inicial = 0
        self.limite_final = tamanho

    def consultar(self):
    def inserir(self):
    def inserir_ordenada(self):
    def remover(self):
    def destruir(self):
    def buscar(self):
    def busca_sequencial(self):
    def busca_binaria(self):

    #Complementares
    def vazia(self):
    def cheia(self):
    















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
from Tabelas import Table
tamanho_tabela = 5
tabela = Table(tamanho_tabela) # Inicializa a tabela com tamanho 3 

tabela.insert("xyz", "abc") #Insere um valor e uma key
tabela.insert("dfg","dfb") #Insere um valor e uma key
tabela.insert("ffg","dfb") #Insere um valor e uma key
tabela.insert("hfg","dfb") #Insere um valor e uma key
tabela.insert_sort("abc","dfb") #Insere um valor e uma key de maneira ordenada
print('Size: '+str(tabela.size())) #Retorna o tamanho da tabela
print(tabela.search('bin', "abc")) # Faz o search pela key passando como primeiro parâmetro o tipo de busca. 'bin' para binária e '' para linear. Retorna a posição
print(tabela.__repr__()) #Retorna a tabela
print(tabela.search_bin("ffg", 0, tamanho_tabela)) #Pesquisa diretamente usando a busca binária. Retorna a posição
print(tabela.search('', 'ffg'))
print(tabela.destroy()) #Destrói a tabela


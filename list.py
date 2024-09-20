"""
Listas em Python
Tipo list - Mutável 
Suporta vários valores de qualquer tipo 
Conhecimento reutilizáveis - índices e fatiamento 
Métodos úteis: 
    append - Adiciona um item ao final 
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido 
    del - Apaga um índice 
    clear - Limpa a lista
    extend - Estende a lista
    + - Concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)

"""

#         01234
#        -54321
string = 'ABCDE' # 5 caracteres (len)

# print(bool([])) # falsy
# print(lista, type(lista))




#         0     1         2          3    4
#        -5    -4        -3         -2   -1    
#lista = [123, True, 'Felipe Bello', 1.2, []]
#lista[-3] = 'Maria' # interagindo com a lista 
#print(lista[2].upper(), type(lista[2]))

""" 
===========APPEND==============
"""
#lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2]) #ctrl ; 
#lista.append(50)
#lista.pop()
#lista.append(60)
#lista.append(70)
#ultimo_valor = lista.pop()
#print(lista, 'Removido,', ultimo_valor)

"""
=============INSERT================
"""
# lista = [10, 20, 30, 40]
# lista.append('Felipe')
# nome = lista.pop()
# lista.insert(0, 5) # primeiro argumento escolhe o índice, e o segundo o argumento que será acrescentado
# lista.insert(5, 'Felipe')
# print(lista)

"""
==========EXTEND============
"""
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6]
# lista_c = lista_a + lista_b
# lista_a.extend(lista_b)
# print(lista_a)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

# nome = 'Luiz'
# nome = 'João'
# print(nome)





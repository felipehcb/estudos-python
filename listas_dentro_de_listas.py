"""
Lista de listas e seus índices

"""

salas = [

     # 0         1
    ['Maria', 'Helena', ], # 0
          
     # 0     
    ['Elaine', ], # 1

     # 0        1        2
    ['Luiz', 'Joao', 'Eduarda', ], # 2 -  #(0, 10, 20, 30, 40)  

]

# print(salas[1][0]) # Elaine

# print(salas[2][1]) # Joao

# print(salas[0][1]) # Helena

# print(salas[2][2]) # Eduarda

# print(salas[2][3][2]) # 20 dentro da tupla

for sala in salas:
    print(f'A sala é {sala}')
    for aluno in sala: 
        print(aluno)
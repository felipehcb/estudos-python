

# nome = input('Qual o seu nome? ')
# print(f'O seu nome é {nome} ')

#=======================================================================
# numero_1 = int(input('digite um número: '))
# numero_2 = int(input('digite outro número: '))

# int_numero_1 = int(numero_1)
# int_numero_2 = int(numero_2)

# print(f'A soma dos números é: {int_numero_1 + int_numero_2}')

#=======================================================================

#entrada = input('Voce quer "entrar" ou "sair"? ')

#if entrada == 'entrar': 
#    print('Voce entrou no sistema')
#elif entrada == 'sair':
#    print('Voce saiu do sistema')  
#else: 
#    print('Voce nao digitou nem entrar e nem sair')    

#=======================================================================

numero_1 = int(input('Digite o primeiro valor: '))
numero_2 = int(input('Digite o segundo valor: '))

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

if (int_numero_1 > int_numero_2):
    print(f'O primeiro valor: {int_numero_1}, é maior que o segundo valor: {int_numero_2}')
elif (int_numero_2 > int_numero_1):
    print(f'O segundo valor: {int_numero_2}, é maior que o primeiro valor: {int_numero_1}')
else: 
    print(f'Os dois valores são iguais: {int_numero_1} e {int_numero_2}')



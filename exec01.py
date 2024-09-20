""" 
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar.. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro. 

"""
# RESPOSTA 

numero = input('Digite um número inteiro: ')

                  # isdigit():

try:

    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('O número que voce digitou é par')

    else: 
        print('O número que voce digitou é ímpar')

except: 
    print('O número que voce digitou nao é inteiro.')




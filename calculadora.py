print('=========================')
print('====== CALCULADORA ======')
print('=========================')


while True:

    operacao = input('Escolha qual será sua operação +-/* ? ')
    a_str = input('Digite um número: ')
    b_str = input('Digite outro número: ')
    resultado: float

    numeros_validos = None
    a=0
    b=0

    try:
        a = float(a_str)
        b = float(b_str)
        numeros_validos = True

    except: 
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'  

    if operacao not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operacao) > 1: 
        print('Digite apenas um operador.')
        continue           

    if operacao == '+':
        resultado = a + b 

    if operacao == '-': 
        resultado = a - b      

    if operacao == '/': 
        resultado = a / b 

    if operacao == '*':
        resultado = a * b 

    print('O resultado da',operacao,'entre',a,'e',b,'é:',resultado)

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break



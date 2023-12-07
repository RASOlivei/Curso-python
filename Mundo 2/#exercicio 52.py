print('Analisar Progreção Aritimetica')

n1 = int(input('digite um numero para saber se ele é primo:'))

c=0
divisores = []

if n1 <= 1:
    print('Não primo.')
else:
    for x in range(2, n1):
        if n1 % x == 0:
            c = c + 1
            divisores.append(x)

    if c == 0: 
        print('Primo.')
        print(divisores, end = '')
    else:
        print('Não primo.')
        print('Divisores: {}'.format(divisores))
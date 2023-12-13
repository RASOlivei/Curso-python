n1 = 0
n2 = 0
n5 = 0

n1 = int(input('Digite 1º valor: '))
n2 = int(input('Digite 2º valor: '))



while not n5 == '5':
    n5 = input('''\n[1]soma
[2]Multiplicação.
[3] Maior.
[4] Novos números.
[5] Sair.
''')

    if '1' in n5:
        print('A soma resulta em: {}'.format(n1+n2))

    if '2' in n5:
        print('A multiplicação resulta em: {}'.format(n1*n2))

    if '3' in n5:
        print('O maior valor digitado: {}'.format(max(n1, n2)))

    if '4' in n5:
        print('Deseja digitar novos números?')
        n1 = int(input('Digite 1º valor: '))
        n2 = int(input('Digite 2º valor: '))

print('Saindo...')
print('\nMultiplicador')
x = int(input('\nInsira um valor da tabuada: '))

for n in range(1, 11):
    print('{} x {} = {}'.format(n, x, (x * n)))
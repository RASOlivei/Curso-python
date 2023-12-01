print('\nMultiplicador')
n = int(input('\nInsira um valor da tabuada: '))
s = 0
s = s + n
for n in range(0, 11):
    print('{} x {} = {}'.format(s, n, (s * n)))
print('Analisar Progreção Aritimetica')

n1 = int(input('digite um numero para saber se ele é primo:'))
total = 0

for c in range(1, n1 + 1):
    if n1 % c ==0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n1, total))

if total == 2:
    print('É por isso ele é primo.')
else:
    print('É por isso ele não é primo!')
num = int(input('Digite um valor entre 0 e 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

if 0 <= num <= 9999:

     print('\nO valor selecionado {}'.format(num))
     print(num)

     print('\nUnidade {}'.format(u))
     print('Dezena {}'.format(d))
     print('Centena {}'.format(c))
     print('Milhar {}'.format(m))
else:    
    print('Valor incorreto.')
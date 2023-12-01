print('Crescente.')

v1 = int(input('Insira o primeiro valor: '))
v2 = int(input('Insira o segundo valor: '))

if v1 != v2:
    print('O maior valor é {} e o menor valor é {}!'.format(max(v1, v2), min(v1, v2)))
else:
   print('Os valores são iguais! {} !'.format(v1))
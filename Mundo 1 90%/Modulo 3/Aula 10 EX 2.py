print('Média Semestral')
n1 = float(input('Nota do primeiro bimestre: '))
n2 = float(input('Nota do segundo bimestre: '))

m = ( n1 + n2 ) / 2

print('A media entre as notas {} e {} resulta em {:.1f}'.format(n1, n2, m))

if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Nota insuficiente, estude mais!')

#=========================SIMPLIFICADO

print('Parabens!' if m >=6 else 'Estude mais!')
print('Média Semestral')
n1 = float(input('Nota do primeiro bimestre: '))
n2 = float(input('Nota do segundo bimestre: '))

m = ( n1 + n2 ) / 2

if 5 <= m <= 6.9:
    print('A media entre as notas {:.1f} e {:.1f} resulta em {:.1f}. RECUPERAÇÃO!'.format(n1, n2, m))
elif  m > 7:
    print('A media entre as notas {:.1f} e {:.1f} resulta em {:.1f}. APROVADO!'.format(n1, n2, m))
else:
    print('A media entre as notas {:.1f} e {:.1f} resulta em {:.1f}. REPROVADO!'.format(n1, n2, m))
print('Média Semestral')


try:
    n1 = float(input('\nNota do primeiro bimestre: '))
    n2 = float(input('Nota do segundo bimestre: '))

    

    if 0 <= n1 <= 10 and 0 <= n2 <= 10:
        m = ( n1 + n2 ) / 2

        print('\nA media entre as notas {:.1f} e {:.1f} resulta em {:.1f}.\n'.format(n1, n2, m))

    else:
        print('\nForneça valores de notas corretamente.')

except ValueError as erro:
    print('\nHouve um erro ao inserir os dados: {}.'.format(erro))
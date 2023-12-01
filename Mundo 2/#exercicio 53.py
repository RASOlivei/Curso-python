print('Palidromo')

n1 = str(input('digite uma frase:')).lower()


if n1.replace(' ', '') == n1.replace(' ', '')[::-1]:
    print('Sim, {}.'.format(n1.replace(' ', '').replace('', ' ')[::-1]))
else:
    print('negativo! {}'.format(n1[::-1]))
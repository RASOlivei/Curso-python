print('\n4Moon')
from datetime import date

y = int(input('Forneça um ano pra avaliação: '))


if y == 0:
    y = date.today().year 

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print('Este ano é bissexto: {}.\n'.format(y))


else:
    print('Este ano não é bissexto: {}.\n'.format(y))


'''
ano = int(input('Insira um ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano bissexto.')
else:
    print('Não é um ano bissexto.')'''
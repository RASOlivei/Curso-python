import random
from random import randint

print('Cara a Cara.\nNeste game você precisa acerta qual número é o correto entre 0 e 5.')

n = int(input('Digite um número: '))

computador = randint(0, 5)

print('=o=' * 20)
num = ['0', '1', '2','3','4','5']
game = random.choice(num)
gamen = str(n)

#print(game)
#print(gamen)

if 0 <= n <= 5:
    print('Certo o valor selecionado é: {}'.format(n))
    print('=o=' * 20)

    if gamen == game:
        print('Parabéns! O valor {} selecionado está correto.'.format(game))

    else:
        print('>> {} << Não foi desta vez, tente novamente. '.format(game))

else:
    print('Valor {} incorreto, poderia digitar novamente. '.format(n))

'''import random

print('Cara a Cara.\nNeste game você precisa acertar qual número é o correto entre 0 e 5.')

n = int(input('Digite um número: '))

numeros = ['0', '1', '2', '3', '4', '5']
num_selecionado = random.choice(numeros)
gamen = str(n)

if 0 <= n <= 5:
    print('Certo, o valor selecionado é: {}'.format(n))

    if gamen == num_selecionado:
        print('Parabéns! O valor {} selecionado está correto.'.format(num_selecionado))
    else:
        print('>> {} << Não foi desta vez, tente novamente. '.format(num_selecionado))
else:
    print('Valor {} incorreto, por favor, digite um número entre 0 e 5.'.format(n))'''

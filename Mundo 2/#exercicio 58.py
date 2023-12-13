import random
from random import randint

print('Cara a Cara.\nNeste game você precisa acerta qual número é o correto entre 0 e 10.')
n = ''
x = 0
computador = randint(0, 10)

while n != computador:
    n = int(input('Digite um número: '))
    x = n + 1

print('Parabéns! Você acertou! Com {} tentativas'.format(x))
print('O número que o computador escolheu foi {}'.format(computador))





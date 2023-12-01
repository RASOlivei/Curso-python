import math 

num = int(input('Insira um valor: '))

raiz = math.sqrt(num)

print('A raiz do valor {}, resulta em {:.2f}'.format(num, (raiz)))
print('A raiz do valor {}, resulta em {}'.format(num, math.ceil(raiz)))
print('A raiz do valor {}, resulta em {}'.format(num, math.floor(raiz)))

#===========================================================================

from math import sqrt

num = int(input('Insira um valor: '))

raiz = sqrt(num)

print('A raiz do valor {}, resulta em {:.2f}'.format(num, (raiz)))
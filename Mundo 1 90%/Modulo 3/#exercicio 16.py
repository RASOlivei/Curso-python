import math

n = float(input("digite um valor: "))

i = math.trunc(n)

print('\nO valor digitado {}, tem a parte inteira {}.'.format(n, i))

print('\nO valor digitado {}, tem a parte inteira {}.'.format(n, math.trunc(n)))

#=============================================================================

from math import trunc

print('\nO valor digitado {}, tem a parte inteira {}.'.format(n, trunc(n)))

#=============================================================================

print('\nO valor digitado {}, tem a parte inteira {}.'.format(n, int(n)))
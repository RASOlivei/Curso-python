import math

a = float(input('Digite um angulo: '))

co = math.cos(math.radians(a))
sen = math.sin(math.radians(a))
tg = math.tan(math.radians(a))

print("\nO angulo {:.0f}°:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(a, sen, co, tg))

#=============================================================================

from math import cos, sin, tan, radians

co = cos(radians(a))
sen = sin(radians(a))
tg = tan(radians(a))

print("\nO angulo {:.0f}°:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}".format(a, sen, co, tg))
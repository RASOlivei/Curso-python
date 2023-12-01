import math

co = float(input("\ndigite um valor do cateto oposto: "))
ca = float(input("digite o valor do cateto adjacente: "))


h = ((ca**2 + co**2))**(1/2)

print('\nO valor C.A. {:.2f}, o valor C.O. {:.2f}.\nResultam na Hipotenusa: {:.2f}.\n'.format(ca, co, h))

#==========================================================

h1 = math.hypot(co, ca)

print('\nO valor C.A. {:.2f}, o valor C.O. {:.2f}.\nResultam na Hipotenusa: {:.2f}.\n'.format(ca, co, h1))

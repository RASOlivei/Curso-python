print('Analise trigonometica')

v1 = float(input('Insira o valor reta Ca: '))
v2 = float(input('Insira o valor reta Co: '))
v3 = float(input('Insira o valor reta H: '))


if v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1:
    print('Estas retas produzem um triangulo.')
else:
    print('Estas retas não produzem um triangulo.')
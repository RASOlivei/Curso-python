'''print('Análise trigonométrica')
v1 = float(input('Insira o valor da reta Ca: '))
v2 = float(input('Insira o valor da reta Co: '))
v3 = float(input('Insira o valor da reta H: '))

if v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1:
    print('Estas retas produzem um triângulo.')
    
    if v1 == v2 == v3:
        print('Formando um triângulo equilátero!')
    elif v1 != v2 != v3 != v1:
        print('Formando um triângulo escaleno!')
    else:
        print('Formando um triângulo isósceles')
else:
    print('Estas retas não produzem um triângulo.')'''

print('Análise trigonométrica')
v1 = float(input('Insira o valor da reta Ca: '))
v2 = float(input('Insira o valor da reta Co: '))
v3 = float(input('Insira o valor da reta H: '))

if v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1:
    print('Estas retas produzem um triângulo: ', end='')
    if v1 == v2 == v3:
        print('Equilátero!')
    elif v1 != v2 != v3 != v1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Estas retas não produzem um triângulo.')
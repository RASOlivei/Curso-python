print('Im-par')

v = int(input('Insira um valor: '))

r = v // 2 % 2
 
if r == 0:
    print('O valor fornecido é par!')
else:
    print('O valor fornecido é impar.')
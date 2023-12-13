i = 0
resultado = 0
n = 0


while True:
    n = int(input('Insira um valor: '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-'*30)

print('FIM.')
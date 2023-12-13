from random import randint

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)


n = 0
pi = ''
total = 0
h = ''
cont = 0


while True:
    pc = randint(0, 10)
    n = int(input('Insira um valor: '))
    pi = str(input('Par ou impar?: ')).upper()
    total = n + pc
    cont += 1

    if total %2 == 0:
        h = 'PAR'
        
    else:
        h = 'IMPAR'
    
    print(f'Você jogou {n} e o computador {pc}. Total de {total} de {h}')
    if h == pi:
        print('Você venceu!')
    else:
        print('Você perdeu! ')
        print(f'Game Over! Você jogou {cont} vezes')
        break

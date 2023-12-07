print('2 in 50')

s = 0
n = 0
i = 0
for c in range(1, 501, 2):
    if c % 3 ==0:    
        n = n + 1 # n += 1
        s = s + c # s += c
    i = i + 1 # n += 1
print('A soma dos {} numeros divisivos por 3 de 0 a 500 resulta em: {}, sendo que o total de numeros impar são {}.'.format(n, s, i))

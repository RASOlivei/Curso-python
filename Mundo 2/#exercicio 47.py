print('2 in 50')

p = int(input('Gostaria de analisar?\n[1] Sim. [2]Não.'))

if p == 1:
    for c in range(2, 51, 2):
        print(c, end=' | ')

else:
    print('Fim.')
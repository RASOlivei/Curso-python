print('2 in 50')

p = int(input('Gostaria de analisar?\n[1] Sim. [2]Não.'))

s = 0

if p == 1:
    for c in range(0, 500, 3):
        #print(c)
        s = s + c
        print(c, s)
else:
    print('Fim.')
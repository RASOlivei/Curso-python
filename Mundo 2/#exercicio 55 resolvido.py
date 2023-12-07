print('Mais ou menos.')

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Insira o {}º peso: '.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
           maior = peso
        if peso < menor:
            menor = peso
print('O maior peso: {} Kg'.format(maior))
print('O maior peso: {} Kg'.format(menor))
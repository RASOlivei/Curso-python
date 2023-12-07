print('Mais ou menos.')

peso = []

for data in range(1, 6):
    d = float(input('Insira o {}º peso: '.format(data)))
    peso.append(d)

print('\nMaior peso:{:.1f} Kg'.format(min(peso)))
print('Menor peso:{:.1f} Kg'.format(max(peso)))
print('Mais ou menos.')

peso = []

for data in range(0, 5):
    d = int(input('Insira um peso: '))
    peso.append(d)

print('\nMaior peso:{}'.format(min(peso)))
print('Menor peso:{}'.format(max(peso)))
import datetime
y = datetime.date.today().year
print('Data Check: {}'.format(y))

maior = []
menor = []

for data in range(0, 7):
    d = int(input('Insira uma data: '))
    if d >= (y-17):
        menor.append(d)
    else:
        maior.append(d)
print('\nMaior:{}'.format(maior))
print('Menor:{}'.format(menor))
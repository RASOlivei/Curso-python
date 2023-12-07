import datetime

y = datetime.date.today().year
print('Data Check: {}'.format(y))

maior = []
menor = []
totmenor = 0
totmaior = 0

for data in range(1, 8):
    d = int(input('Insira a {}º data: '.format(data)))
    if d >= (y-21):
        menor.append(d)
        totmenor += 1
    else:
        maior.append(d)
        totmaior += 1
print('\nSão {} maior:{}'.format(totmaior, maior))
print('São {} menor:{}'.format(totmenor, menor))
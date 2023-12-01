#Condições em Python (if..else)

tempo = int(input('Quantos anos tem seu carro? : '))

#==================SIMPLICAIFCADO
print('Carro novo.'if tempo <= 3 else 'Carro velho.')



if tempo <= 3:
    print('Carro novo.')
else:
    print('Carro velho.')

print('--FIM--')
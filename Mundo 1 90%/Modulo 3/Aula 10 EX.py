#Condições em Python (if..else)

nome = str(input('Qua o seu nome? : '))

#==================SIMPLICAIFCADO
#print('Carro novo.'if nome <= 3 else 'Carro velho.')

#===================PADRÃO

if nome == 'RASO':
    print('Programador Identificado.')
else:
    print('Usuario identificado.')

print('Bom dia, {}.'.format(nome))
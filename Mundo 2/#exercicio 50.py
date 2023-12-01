'''print('\n Par dos três.')

#Criando uma lista pros dados:
soma = []
for n in range(0, 3):
    z = int(input('Insira um valor: '))
    soma.append(z)
#print(soma)

#Somando os dados pares na lista:
npar = [ x for x in soma if x % 2 == 0]

#Apresentando dados:
if npar:
    np = sum(npar) 
    print('Os numeros pares inseridos foram: {}'.format(np))
else:
    print('Nenhum numero par digitado.')
'''
print('\n Par dos Seis.')

# Somando os dados pares na lista:
npar = []
for n in range(0, 6):
    z = int(input('Insira um valor: '))
    if z % 2 == 0:
        npar.append(z)

# Apresentando dados:
if npar:
    np = sum(npar)
    print('Os numeros pares somados resulta: {}'.format(np))
else:
    print('Nenhum numero par digitado.')
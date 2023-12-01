#Exercicio 15

print('\nAuto Location')

d = int(input('\nQuantos dias utilizou o carro: '))

km = float(input('Quantos kilometros foram percorridos: '))

cd = d * 60

ckm = km * .15

r = cd + ckm

print('\nSegundo os dados fornecidos o carro foi utilizado por {} dias.\nCustando R${:.2f}.'.format(d, cd))
print('\nDurante os {} dias, foi percorrido {} km.\nCustando R${:.2f}.'.format(d, km, ckm))
print('\nO valor total é R${}!'.format(r))
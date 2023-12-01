#aula 7
#nome = str(input('Qual o seu nome? '))

#print('Prazer em lhe conhecer {:=^20}.'.format(nome)) 

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {},\no produto é {},\na divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} é a potência {}'.format(di, e))
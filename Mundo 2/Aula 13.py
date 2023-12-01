#Estrutura de repetição for

for c in range(1, 6):
    print('Oi')
print('fim.')

print('=' * 11)
for c in range(0, 9):
    print(c)

print('=' * 11)
for c in range(6, 0, -1):
    print(c)

print('=' * 11)
for c in range(0, 20, 2):
    print(c)

print('=' * 11)
n = int(input('Insira um numero: '))
for c in range(0, n+1):
    print(c)
print('fim.')

print('=' * 11)
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)
print('fim.')

print('=' * 11)
s = 0
for c in range(0, 3):
    n = int(input('Insira um valor: '))
    s = s + n  # ou s += n
print('Somatoria: {}'.format(s))
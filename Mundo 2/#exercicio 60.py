n = int(input('Calcular Fatorial de: '))

resultado = 1
count = 1

while count <= n:
    resultado = resultado * count
    count = count + 1

print('O fatorial de {} é {}'.format(n, resultado))

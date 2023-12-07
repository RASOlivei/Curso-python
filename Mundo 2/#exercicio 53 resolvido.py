print('Palíndromo')

n1 = str(input('digite uma frase:')).lower().strip()

palavras = n1.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('É um palíndromo.')
    print(junto, inverso)
else:
    print('Não é palíndromo.')
    print(junto, inverso)

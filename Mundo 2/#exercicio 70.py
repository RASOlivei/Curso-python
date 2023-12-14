from random import randint

print('-=-' * 20)
print('Cadastro Analítico.')
print('-=-' * 20)

prox = ''
prod = 0
valor = 0
total = 0
prodmin = float('inf')
prodnome = ''
prod1000 = 0


while prox != 'N':
    if prox == 'N':
        break
    prod = str(input('Digite o nome do produto: ')).strip()
    valor = int(input('Digite o valor: '))
    prox = str(input('Quer continuar? [S/N] ')).upper().strip()

    total += valor
    if valor > 1000:
        prod1000 += 1

    if valor < prodmin:
        prodmin = valor
        prodnome = prod


print('-=-' * 20)
print(f'O total da compra foi de R${total:.2f}.')
print(f'E temos {prod1000} produtos com valor maior que R$1000.00 reais.')
print(f'O produto mais barato foi {prodnome} com o valor de R${prodmin:.2f} reais. ')
print('-=-' * 20)
print('Fim.')
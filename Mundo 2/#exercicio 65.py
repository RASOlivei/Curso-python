resp = 'S'
media = 0
soma = 0
quant = 0
maior = 0
menor = 0


while resp in 'Ss':
    n = int(input('Digite um número : '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N]: ').upper().strip()[0])
media = soma / quant

print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
print('Fim do programa.')

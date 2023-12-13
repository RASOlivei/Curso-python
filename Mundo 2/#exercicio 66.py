n = 0
cont = 0
soma = 0

while n != 999:
    n = int(input('Digite um número [999 pra parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n

print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')


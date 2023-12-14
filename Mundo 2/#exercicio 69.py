from random import randint

print('-=-' * 20)
print('Cadastro Analítico.')
print('-=-' * 20)

prox = ''
Maior_de_idade = 0
homens = 0
Mulheres_20 = 0

while prox != 'N':
    if prox == 'N':
        break
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()
    prox = str(input('Quer continuar? [S/N] ')).upper().strip()

    if sexo == 'F':
        if idade < 20: 
            Mulheres_20 += 1
    if idade > 18:
        Maior_de_idade += 1
    if sexo == 'M':
        homens += 1

print('-=-' * 20)
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {Maior_de_idade} mais de 18 anos.')
print(f'E temos {Mulheres_20} mulheres com menos de 20 anos.')

print('Fim.')
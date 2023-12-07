print('Verificando...')

mediaidade = 0
somaidade = 0
maioridadehomem = 0
nomevelho = ''
total_mulher_20 = 0

for p in range(1, 5):
    print('====={}º Pessoa ====='.format(p))
    nome = str(input('nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Genero [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo in 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        total_mulher_20 += 1


mediaidade = somaidade / 4

print('A média da idade do grupo é {}'.format(int(mediaidade)))
print('O homem mais velho tem {} e se chama {}.'.format(maioridadehomem, nomevelho))
print('No total são {} mulheres com menos de 20 anos.'.format(total_mulher_20))
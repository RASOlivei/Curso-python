import random
print('Jokenpô')
print('Pedra, Papel ou Tesoura!?')
v = str(input('Qual a sua escolha: '))
escolha = v.lower()
pc = random.choice(['pedra', 'papel', 'tesoura'])
if v == pc:
    print('Empate')
if pc == 'pedra':
    if escolha == 'papel':
        print('Você perdeu!')
    if escolha == 'tesoura':
        print('Você ganhou!')
if pc == 'papel':
    if escolha == 'pedra':
        print('Você ganhou!')
    if escolha == 'tesoura':
        print('Você perdeu!')
if pc == 'tesoura':
    if escolha == 'pedra':
        print('Você perdeu!')
    if escolha == 'papel':
        print('Você ganhou!')
print('=*=' * 11)
print('Computador jogou {}'.format(pc))
print('Você jogou {}'.format(escolha))
print('=*=' * 11)
print('Fim do jogo!')
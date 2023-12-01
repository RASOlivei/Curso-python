import math
import emoji
import random

print(emoji.emojize('\nSorteio do Professor!:man_teacher:\n'))

print('Nomes: ')
n1 = str(input('\nPrimeiro Aluno: '))
n2 = str(input('Segundo Aluno: ')) 
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: ')) 

alunos = [n1, n2, n3, n4]

r = random.choice(alunos)

print(emoji.emojize('O escolhido é {}! :rocket:'.format(r)))
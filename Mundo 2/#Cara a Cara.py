#Cara a Cara
import random

print('Cara a Cara.\nAs condições deste programa é acerta o número selecionado entre 0 e 5.')

n = int('Digite um número: ')
cpu = ['0','1', '2','3','4','5'] 
game = random.choices(cpu)


if 0 <= n <= 5:
    print('Certo, o valor selecionado é {}'.format(n))

    if n == game:
        print('O Valor selecionado é o correto!') 
    else:
        print('Valor selecionado incorreto, tente novamente.')   


else:
    print('insira um valor correto.')
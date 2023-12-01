print('Contagem Regressiva!')
from time import sleep
import emoji

p = int(input('Começar contagem: [1] Sim ou [2] Não.'))

if p == 1:
    for c in range(1,11):
        print(c)
        sleep(1)
    print(emoji.emojize(':rocket: UAU! :rocket:'))
else:
    print('Fim.')
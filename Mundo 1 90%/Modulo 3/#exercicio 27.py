c = str(input('Insira um nome completo: ')).strip()

nome = c.split()
print(nome)


print('A primeira letra palavra: {}'.format(nome[0]))
print('A Ultima letra palavra: {}'.format(nome[len(nome)-1]))


#GPT
'''Seu código parece estar correto e faz o que você deseja, que é contar quantas vezes a letra 'a' aparece na palavra fornecida pelo usuário. Aqui está uma análise do código:

c = str(input('Insira uma palavra: ')): Esta linha solicita ao usuário que insira uma palavra e armazena essa palavra na variável c.

palavra = c.lower(): Esta linha converte a palavra inserida para letras minúsculas usando o método lower(). 
Isso garante que a contagem da letra 'a' não seja sensível a maiúsculas e minúsculas.

print('Esta palavra tem {}, a letra "a"!'.format(palavra.count('a'))):
 Aqui, o código usa o método count() para contar quantas vezes a letra 'a' aparece na palavra convertida para minúsculas. 
 Em seguida, exibe o número de ocorrências na frase de saída.

Esse código está correto para contar o número de vezes que a letra 'a' aparece na palavra fornecida pelo usuário, independentemente
 de estar em letras maiúsculas, minúsculas ou uma combinação delas.'''
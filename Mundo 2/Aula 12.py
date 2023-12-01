#Condições Alinhadas.

nome = str(input('Qual seu nome: '))

if nome == 'RASO':
    print('{}! O programador!'.format(nome))

elif nome == 'João' or nome == 'Maria' or nome == 'Pedro':
    print('Usuario seu nome é bem comum, {}.'.format(nome))

else:
    print('Olá, usuario {}.'.format(nome ))
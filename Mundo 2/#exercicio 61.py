print('Analisar Progreção Aritimetica v2.0')

primeiro = int(input('Insira o termo: '))
razao = int(input('insira a razão: '))


termo = primeiro
cont = 1

while cont <= 10:
    print('{}→ '.format(termo), end='')
    termo = termo + razao
    cont += 1

print('FIM.')


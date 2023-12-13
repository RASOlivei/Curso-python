print('Analisar Progreção Aritimetica v3.0')

primeiro = int(input('Insira o termo: '))
razao = int(input('insira a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}→ '.format(termo), end='')
        termo = termo + razao
        cont += 1
    print('PAUSA.')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão com {} termos inseridos.'. format(total))
print('FIM.')

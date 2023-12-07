print('Analisar Progreção Aritimetica')

termo = int(input('Insira o termo: '))
razao = int(input('insira a razão: '))
decimo = termo + (10 - 1) * razao

if razao and termo > 0:
    for c in range(termo, decimo + razao, razao):
        print(c, end=' ¬ ')

else:
    print('Fim.')
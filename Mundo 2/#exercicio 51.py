print('Analisar Progreção Aritimetica')

termo = int(input('Insira o termo: '))
razao = int(input('insira a razão: '))

quinto = []
x = razao * 10

if razao > 0:
    for c in range(termo, x , razao):
        quinto.append(c)
        print(c)
    print(quinto[0:11])
else:
    print('Fim.')
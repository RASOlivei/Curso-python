#exercicios 12

print('\nPromoçõa 5% em todo o estoque!')

v = float(input('\nInsira o valor: R$'))

d = (v * 0.05)

r = v - d

print('\nO valor do produto {:.2f}, com o desconto o produto custará: \nR${:.2f}!\n'.format(v, r))

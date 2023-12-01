#exercicio 13

print('\nAjuste salárial.')

v = float(input('\nInsira o valor salarial atual: R$'))

a = v * (15 / 100)

aa = v - a

r = v + a

print('\nO ajuste aplicado será de 15%.\nO valor atualizado será de R${:.2f}.\nSendo o valor de R${:.2f} sobre o salário informado: R${:.2f}.\n'.format(r, a, v))
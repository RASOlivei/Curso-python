print('Analise Salarial.')

v = float(input('Valor Salarial: R$'))

if v <= 1250:
    print('O aumento será de 15% sobre o valor R$ {:.2f}.\nTendo o valor atualizado: R${:.2f}'.format(v, (v * 0.15) + v))
else:
    print('O aumento será de 10% sobre o valor R$ {:.2f}.\nTendo o valor atualizado: R${:.2f}'.format(v, (v * 0.1) + v))

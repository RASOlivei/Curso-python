print('Evento Promoção')
v = float(input('\nQual o valor do produto: R$'))
print('Selecione a forma de pagamento')
pay = int(input('R$ {:.2f}.\n01.à vista dinheiro ou cheque  02.cartão à vista  03.cartão parcelado : '.format(v)))
if pay == 1:
    print('O valor total a ser pago é: R$', v * 0.9)
if pay == 2:
    print('O valor total a ser pago é: R$', v * 0.95)
if pay == 3:
    x = int(input('\nEm quantas vezes: '))
    if x == 2:
        print('O valor a ser pago será 2 vezes de R${:.2f}. Total = R${:.2f}.'.format((v/2), v))
    if x >= 3:
        print('O valor a ser pago será {:.2f} vezes de R${:.2f}. Total = R${:.2f}.'.format(x, (v + v * 0.2) / x, (v + v * 0.2)))
else:
    print('\nVenda fechada.')
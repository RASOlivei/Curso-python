print('Indice de Massa Muscular.')


p = float(input('Qual o seu peso: '))
a = float(input('Qual a sua idade: '))

print('Os dado fornecidos foram: eso {:.2f} Kg e {:.2f} altura.\n'.format(p, a))

imc = (p / (a ** 2))

if imc < 18.5:
    print('Sua categoria : abaixo do peso IMC {:.2f}.'.format(imc))
elif 18.5 <= imc <= 25:
    print('Sua categoria : peso ideal IMC {:.2f}.'.format(imc))
elif 25 <= imc <= 30:
    print('Sua categoria : sobrepeso IMC {:.2f}.'.format(imc))
elif 30 <= imc <= 40:
    print('Sua categoria : obesidade IMC {:.2f}.'.format(imc))
elif imc > 40:
    print('Sua categoria : obesidade morbida IMC {:.2f}.'.format(imc))
else:
    print('Erro!')

print('Radandam')

v = float(input('\nQual a velocidade do veiculo (km/h): '))

r = v - 80

multa = r * 7



if v >= 80.0:
    print('\nA velocidade excedeu 80km/h. O valor da multa será de R$ {:.2f} reais.'.format(multa))
else:
    print('\nA velocidade está dentro do limite permitido pela via.\n')
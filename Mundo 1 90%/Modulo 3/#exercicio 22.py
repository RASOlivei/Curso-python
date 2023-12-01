n = str(input('Insira o nome completo: '))

print(n.lower())
print(n.upper())

nf = n.split()

print('Este nome possui {} letras.'.format((len(n.replace(' ', '')))))
print('O peimeiro no tem {} letras.'.format(len(nf[0])))
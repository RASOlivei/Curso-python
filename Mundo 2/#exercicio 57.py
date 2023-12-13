n = ''
n = input('Digite seu sexo: ').upper().strip()
while n not in 'MmFf':
    n = str(input('Digite um sexo correto: ')).upper().strip() 

print('Sexo {} registrado com sucesso!'.format(n))
print('Fim')
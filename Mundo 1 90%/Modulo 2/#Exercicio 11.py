#Exercicio 11

print("Colors S.A.")

l = float(input('Qual largura da parede: '))
a = float(input('Qual a altura da parede: '))

m2 = (l * a)

t = (m2 / 2)



print('\nA parede possui {}m², sendo assim será necessario {:.1f} litros de tinta.'.format(m2, t))

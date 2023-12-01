#Fatiamento
frase = 'Curso em Video Python'

print(frase[9])

print('''Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().''')



print(frase[9:13])

print(frase[9:21])

print(frase[9:21:2])

print(frase[:5])
 
print(frase[15:])

print(frase[9::3])

#Analise

print(len(frase))

print(frase.count('o'))

print(frase.find('deo'))
print(frase.lower().find('video'))

print(frase.find('Android'))
#frase  = frase.replace('Python', 'Android')
#print(frase)

print('Curso' in frase)

print(frase.replace('Python', 'Android'))

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

f = ('   Aprenda Python  ')

print(f.strip())
print(frase.strip())





print(f.rstrip())
print(f.lstrip())

print(frase.split())

print('-'.join(frase))

dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3])
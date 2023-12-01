#Fatiamento
frase = 'Curso em Video Python'

print(frase[9])

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


print(frase.find('Android'))

print('Curso' in frase)

print(frase.replace('Python', 'Android'))

print(frase.upper())

print(frase.lower())

print(frase.capitalize())

print(frase.title())

f = ('   Aprenda Python  ')

print(f.strip())

print(f.rstrip())
print(f.lstrip())

print(frase.split())

print('-'.join(frase))
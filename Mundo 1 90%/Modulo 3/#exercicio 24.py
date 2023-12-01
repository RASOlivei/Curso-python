c = str(input('Insira um nome de Cidade: ')).strip()

palavra = c.lower()

#Aula
#================================================================
if c[:5].lower() == 'santo':
       print('Este nome inicia com a palavra Santo!') #Aula

else:
       print('Este nome não inicia com a palavra Santo!')
#================================================================
if 'santo' in palavra:
        print('Está cidade tem a palavra Santo!')
        print(c)
  
else:
        print(c)
#================================================================
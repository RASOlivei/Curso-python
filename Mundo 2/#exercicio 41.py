print('Condecorações.')
import datetime

v = int(input('Olá diga qual o ano de nascimento pra analise de sua categoria: '))


#Definir dia atual:
today = datetime.date.today()

#Coletar apenas o ano:
comp = int(today.strftime("%Y"))

#Calculo entre anos:
comp1 = comp - v

#Apresentação da data atual:
print('\nCerto com sua idade podemos definir que a presente data :{}'.format(today.strftime("%d/%m/%Y")))

print('Sua idade atual: {} anos.\n'.format(comp1))

if comp1 < 9:
    print('Sua categoria é mirrim: {} anos.'.format(comp1))
elif 10 <= comp1 <= 14:
    print('Sua categoria é infantil: {} anos.'.format(comp1))
elif 15 <= comp1 <= 19:
    print('Sua categoria é Junior: {} anos.'.format(comp1))
elif comp1 == 20:
    print('Sua categoria é sênior: {} anos.'.format(comp1))
else:
    print('Sua categoria é master: {} anos.'.format(comp1))

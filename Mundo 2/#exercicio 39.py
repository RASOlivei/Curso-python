print('Alistamento.')
import datetime
sex = str(input('Qual seu sexo? [M/F]: ')).upper()

if sex == 'M':
    print('Você é masculino.')
    v = int(input('Olá diga qual o ano de nascimento pra analise de alistamento: '))

    #Definir dia atual:
    today = datetime.date.today()
    year = datetime.date.today().year

    #Coletar apenas o ano:
    comp = int(today.strftime("%Y"))

    #Calculo entre anos:
    comp1 = comp - v

    #Calculo da diferença:
    dif = comp1 - 18

    #Apresentação da data atual:
    print('\nCerto com sua idade podemos definir que a presente data :{}'.format(today.strftime("%d/%m/%Y")))
    print('Sua idade atual: {} anos.\n'.format(comp1))
    
    if comp1 == 18:
        print('Está em ano de alistamento para o exercito brasileiro!')
    elif comp1 > 18:
        print('Você ultrapassou a idade de alistamento em {} ano(s), verifique sua condição no quartel mais proximo.'.format(comp1 - 18))
        print('Seu alistamento foi no ano: {}'.format((18 -  comp1) + year))
    else:
        print('Não está em periodo de alistamento. Faltam {} ano(s)'.format(18 -  comp1))
        print('Seu alistamento será no ano: {}'.format((18 -  comp1)+ year))
else:
    print('Você é feminino, alistamento não obrigtorio.')
    print('Selva!')
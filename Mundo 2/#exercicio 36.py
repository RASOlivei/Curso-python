#Condições Alinhadas.
print('#' * 9)
print('# Cubos #')
print('#' * 9)

print('Simularemos seu pedido de emprestimo.\nPra isto precisaremos de alguns dados.')
house = int(input('Qual o valor da casa? R$'))
money = int(input('Qual o valor do seu salário? R$'))
year = int(input('Quantos anos de financeamento?:'))

#parametro de valor
porc = (money * 0.3)

#Anos
parcel = year * 12

#Prestação
x = house / parcel


if x <= porc:
    print('\n\nParabéns! Os criterios de financeamento foram atendidos.')
    print('\nO valor mensal será de {:.2f}, em {:.0f} vezes. Seja feliz.'.format(x, parcel))
    print('Este financeamento comprometerá R${:.2f} do seu salário, sendo que 30% dele seria: R${:.2f}.\n'.format(x, money * 0.3))

else:
    print('\nSeus dados não atendem aos requisitos de financeamento.\nO Valor minimo de pagamento seria de R${:.2f}, atual R${:.2f}.\n'.format(x, porc))

''' 
Claro, seu código parece estar bem estruturado e visa simular um pedido de empréstimo com base no valor da casa, salário e quantidade de parcelas fornecidos pelo usuário. Vou fornecer uma análise detalhada do seu código:

Interação com o usuário:

Você utiliza a função input() para solicitar ao usuário os valores relevantes para o cálculo do empréstimo, como o valor da casa, o salário e o número de parcelas desejadas.
Cálculo dos parâmetros:

Você calcula a porcentagem de 30% do salário (money * 0.3) para determinar o limite de pagamento mensal, considerando a regra usual de que o valor da parcela do empréstimo não deve exceder 30% do salário.
Condição alinhada:

O bloco if-else verifica se o valor da parcela do empréstimo (x) é menor ou igual a 30% do salário (porc). Se for, o programa informa que os critérios de financiamento foram atendidos e fornece detalhes sobre o valor da parcela.
Caso contrário, se o valor da parcela exceder os 30% do salário, o programa informa que os dados não atendem aos requisitos de financiamento e sugere o valor mínimo de pagamento aceitável.
Saída formatada:

Você formata adequadamente a saída para exibir os valores relevantes com duas casas decimais e mensagens descritivas, fornecendo uma resposta clara ao usuário.
No geral, o código parece estar bem estruturado e lógico, verificando se o usuário atende aos critérios mínimos de financiamento com base nos valores inseridos. É importante notar que este é um modelo básico e pode ser expandido com mais condições ou informações para uma análise de crédito mais completa.  '''
print('Calculo de imposto de renda\n')

bruto = float(input('Informe seu sálario bruto: R$'))

# Calculo INSS
print('Tabela INSS')
print('-' * 50)
print('Faixa de salário      | Alíquota(%) | Valor devido (R$)')
print('0 até 1.320,00        |     7,5     | 99,00')
print('1.320,01 até 2.571,29 |     9       | 112,62')
print('2.571,30 até 3.856,94 |     12      | 154,28')
print('3.856,95 até 7.507,49 |     14      | 511,07')
print('-' * 50)

base = 0.0

#faixa 1
if bruto <= 1320.00:
    base += (1320 - bruto) * 0.075
    anual = base * 12

#faixa 2
elif bruto > 1320.00 and bruto <= 2571.29:
    redondou = (bruto - 1320.01) * 0.09
    redondou = round(redondou, 2)
    base += redondou + 99
    anual = base * 12

#faixa 3
elif bruto > 2571.29 and bruto <= 3856.95:
    redondou = (bruto - 2571.3) * 0.12
    redondou = round(redondou, 2)
    base += redondou + 99 + 122.62
    anual = base * 12

#faixa 4
elif bruto > 3856.95 and bruto <= 7507.49:
    redondou = (bruto - 3856.95) * 0.14
    redondou = round(redondou, 2)
    base += redondou + 99 + 112.62 + 154.28
    anual = base * 12

#faixa 5
else:
    base += 876.97
    anual = base * 12

print('O tanto que você paga de INSS é: R${:.2f}'.format(base))
print('Anualmente você paga: R${:.2f}'.format(anual))

r = input('\nDeseja continuar? (s/n) ')
if r == 'n':
    exit()
else:
    print(' ')

print('Tabela IRRF')
print('-' * 50)
print('Faixa de salário      | Alíquota(%) | Dedução (R$)')
print('0 até 2.112,00        |      0      | 0') #1
print('2.112,01 até 2.826,65 |     7,5     | 158,40') #2
print('2.826,66 até 3.751,05 |     15      | 370,40') #3
print('3.751,06 até 4.664,68 |     22,5    | 651,73') #4
print('Acima de 4.664,68     |     27,5    | 884,96') #5
print('-' * 50)

imposto = 0.0
deducao = 0.0

#faixa 1
if bruto <= 2112.00:
    print('Você está insento do IRRF')

#faixa 2
elif bruto > 2112 and bruto <= 2826.65:
    imposto += ((bruto - base) * 0.075) - 158.40

#faixa 3
elif bruto > 2826.65 and bruto <= 3751.05:
    imposto += ((bruto - base) * 0.15) - 370.40

#faixa 4
elif bruto > 3751.05 and bruto <= 4664.68:
    imposto += ((bruto - base) * 0.225) - 651.73

#faixa 5
elif bruto > 4664.68:
    imposto += ((bruto - base) * 0.275) - 884.96

salario = bruto - imposto - base
porcentagem = (salario / bruto) * 100
print('\nO tanto que você paga de IRRF é: R${:.2f}'.format(imposto))
print('Seu salário líquido é: R${:.2f}'.format(salario))
print('Porcetagem do salário bruto que você recebe é: {:.2f}%\n'.format(porcentagem))
print('=='*20)
print('{:^40}'.format('Banco CEV'))
print('=='*20)

saque = int(input('Que valor você quer sacar? R$ '))

if saque >= 50:
    cedulas50 = int(saque / 50)
    saque = saque - (cedulas50 * 50)
    print(f'Total de {cedulas50} cédulas de R$ 50')
if saque >= 20:
    cedulas20 = int(saque / 20)
    saque = saque - (cedulas20 * 20)
    print(f'Total de {cedulas20} cédulas de R$ 20')
if saque >= 10:
    cedulas10 = int(saque / 10)
    saque = saque - (cedulas10 * 10)
    print(f'Total de {cedulas10} cédulas de R$ 10')
if saque >= 1:
    cedulas1 = saque
    print(f'Total de {cedulas1} cédulas de R$ 1')

print('=='*25)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

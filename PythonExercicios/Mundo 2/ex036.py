casa = float(input('Qual o valor da casa? '))
salario = float(input('Quanto é o seu salário? '))
anos = int(input('Quantos anos precisa pra pagar? '))
prestacao = casa / (anos * 12)

print('As parcelas do seu emprestimo de {} será de {:.2f}.'.format(casa, prestacao))

if prestacao <= 30/100 * salario:
    resultado = 'Aprovado'
else: 
    resultado = 'Reprovado'

print('Devido a isso o seu emprestimo será {}'.format(resultado))

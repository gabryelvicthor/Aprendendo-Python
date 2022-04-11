print('-=-' * 10)
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('-=-' * 10)

media = (nota1 + nota2)/2

print('Após somar a notas {} e {} do aluno, a sua média é: {}'.format(nota1, nota2, media))

if  media >= 7:
    resultado = 'Aprovado'
elif media >= 5 and media < 7:
    resultado = 'Recuperação'
else:
    resultado = 'Reprovado'

print('O aluno está {}'.format(resultado))

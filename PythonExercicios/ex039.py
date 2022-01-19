from datetime import date


ano = int(input('Digite seu ano de nascimento: '))
sexo = input('Qual seu sex? ("H", "M") ').lower().strip()
idade = date.today().year - ano
print('Quem nasceu no ano de {} tem ou fará {} anos.'.format(ano, idade))

if sexo == 'h':
    if idade > 18:
        print('Você já deveria ter se alistado há {} anos'.format(idade - 18))
    elif idade < 18:
        print('Ainda falta {} anos para você se alistar. '.format(18 - idade))
    else:
        print('Você deve se alistar nesse ano de {} '.format(date.today().year))
else:
    print('Você não precisa se alistar no exercito. ')
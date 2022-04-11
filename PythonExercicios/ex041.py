from datetime import date


nasc = int(input('Digite seu ano de nascimento: '))
nasc = date.today().year - nasc

print('Você possui {} anos'.format(nasc))

if nasc <= 9:
    categoria = 'Mirin'
elif nasc <= 14:
    categoria = 'Infantil'
elif nasc <= 19:
    categoria = 'Junior'
elif nasc <= 25:
    categoria = 'Sênior'
elif nasc > 25:
    categoria = 'Master'

print('Está na categoria: {}'.format(categoria))
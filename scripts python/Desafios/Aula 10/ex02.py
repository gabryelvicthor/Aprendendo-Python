n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segundda nota: '))
n3 = (n1 + n2) / 2

print('Sua nota foi: {:.2f}'.format(n3))

if n3 < 6:
    print('Você não conseguiu nota suficiente :(')
else:
    print('Parabéns, você conseguiu passar na matéria :)')

print('Parabéns!' if n3 >= 6 else 'Estude mais!')

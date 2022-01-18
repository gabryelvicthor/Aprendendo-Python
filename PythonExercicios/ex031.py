dis = float(input('Qual a distância da sua viagem? '))
print('Você está preste a começar uma viagem de {:.2f} Km.'.format(dis))

if dis <= 200:
    print('O valor da viagem é de: {:.2f}'.format(dis * 0.50))
else:
    print('O valor da viagem é de: {:.2f}'.format(dis * 0.45))

print('Que viagem curta!' if dis <= 200 else 'Que viagem longa!')

print('-=' * 8)
print('Gerador de PA')
print('-=' * 8)

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
i = 0
j = cont = 10

while not j == 0:
    while not i == j:
        print('{} > '.format(p), end= '')
        p += r
        i += 1
    print('PAUSA')
    j = int(input('Quantos termos você quer mostrar a mais? '))
    i = 0
    cont += j

print('Progressão finalizada com {} termos mostrados.'.format(cont))

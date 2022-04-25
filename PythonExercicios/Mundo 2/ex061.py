print('-=' * 8)
print('Gerador de PA')
print('-=' * 8)

p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
i = 0
while not i == 10:
    print('{} > '.format(p), end= '')
    p += r
    i +=1
print('FIM')

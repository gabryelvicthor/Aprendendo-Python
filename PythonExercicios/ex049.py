n1 = int(input('Digite um valor inteiro: '))
print('\nAqui está a tabuada do número {}: '.format(n1))

for i in range(1, 11):
    print('{} x {:2} = {}'.format(n1, i,  n1 * i))
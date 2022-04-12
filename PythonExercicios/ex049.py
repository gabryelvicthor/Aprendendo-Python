n1 = int(input('Digite um valor inteiro: '))
print('\nAqui está a tabuada do número {}: '.format(n1))
print('='  * 13)

for i in range(1, 11):
    print('{}x {:=^10}'.format(i, n1 * i))
    
print('='  * 13)
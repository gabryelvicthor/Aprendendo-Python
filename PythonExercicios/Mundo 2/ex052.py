cont = 0

n1 = int(input('Digite um número: '))

for i in range(1, n1 + 1):
    if n1 % i == 0:
        print('\033[32m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(i), end=' ')

print('\n\033[mO número {} foi divisível {} vezes'.format(n1, cont))    

if cont == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')
    
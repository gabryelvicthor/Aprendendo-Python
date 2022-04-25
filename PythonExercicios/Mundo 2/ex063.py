print('~~~~' * 6)
print('Sequência de Fibonacci')
print('~~~~' * 6)
termos = int(input('Quantos termos você quer mostrar? '))
i = 2
t1 = 0
t2 = 1
print('~~~~' * 10)
print('0 - 1', end='')
while i < termos:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    i += 1
    t1 = t2
    t2 = t3
print(' - FIM')
print('~~~~' * 10)

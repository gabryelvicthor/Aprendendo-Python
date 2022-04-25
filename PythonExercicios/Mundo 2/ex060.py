# from math import factorial
# factorial(num)

print('Digite um número para', end=' ')
num = int(input('calcular seu fatorial: '))
print('Calculando {}! = {}'.format(num, num), end='')
resultado = 1
while not num == 1:
    print(' x {}'.format(num - 1), end='')
    resultado *= num
    num -= 1
print(' = {}'.format(resultado))


print('Digite um número para', end=' ')
num = int(input('calcular seu fatorial: '))
print('Calculando {}! = {}'.format(num, num), end='')
resultado = 1
for f in range(num , 1, -1):
    print(' x {}'.format(f - 1), end='')
    resultado *= f
print(' = {}'.format(resultado))
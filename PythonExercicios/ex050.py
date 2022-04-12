p = 0
im = 0

for i in range(0, 6):
    n = int(input('Digite um número para ser somado: '))
    if n % 2 == 0:
        p += n
    else:
        im += n

print('A soma dos números pares é: {}'.format(p))
print('A soma dos números impares é: {}'.format(im))
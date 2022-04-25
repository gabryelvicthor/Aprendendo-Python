p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
resultado = p
for i in range(1, 11):
    print('{}: {}'.format(i, resultado ))
    resultado += r
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

menor = n1
maior = n1
if menor > n2:
    menor = n2
if menor > n3:
    menor = n3

if maior < n2:
    maior = n2
if maior < n3:
    maior = n3

print('O menor valor é: {}'.format(menor))
print('O maior valor é: {}'.format(maior))
from pickletools import float8


print('-=-' * 15)
print('Analizador de Triângulos')
print('-=-' * 15)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))

if n1 < n2 + n3 and n2 < n3 + n1 and n3 < n1+ n2:
    print('Os seguimentos acima PODERM FORMAR um triângulo.')
else:
    print('Os seguimentos acima NÃO PODERM FORMAR um triângulo.')
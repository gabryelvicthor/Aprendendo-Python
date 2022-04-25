from distutils import core


num = int(input('Informe um número: '))
print('Analisando o número {}'.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

cores = {'limpa':'\033[m', 
        'verde':'\033[32m', 
        'vermelho':'\033[31m'}

print('Unidade: {}{}'.format(u,cores['verde']))
print('Dezena: {}'.format(d))
print('Centena: {}{}'.format(c, cores['limpa']))
print('Milhar: {}'.format(m))

# num = input('Informe um número: ')
# print('Analisando o número {}'.format(num))
# print('Unidade: {}'.format(num[0]))
# print('Dezena: {}'.format(num[0]))
# print('Centena: {}'.format(num[1]))
# print('Milhar: {}'.format(num[0]))
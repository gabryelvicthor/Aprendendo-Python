temperatura = float(input('Informe a temperatura em ºC: '))

cores = {'limpa':'\033[m', 
        'verde':'\033[32m', 
        'vermelho':'\033[31m'}

print('A temperatura de {}{:.1f}{}ºC corresponde a {}{:.1f}{}ºF!'.format(cores['vermelho'], temperatura, cores['limpa'], cores['vermelho'], (9 * temperatura) / 5 + 32, cores['limpa']))

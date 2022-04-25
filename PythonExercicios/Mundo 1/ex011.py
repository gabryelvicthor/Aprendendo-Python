largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = altura * largura
tinta = area / 2
print('Area: {} m2'.format(area))
print('Com as medidas {:.2f}x{:.2f} a quantidade de litros de tinta necessários é: {:.2f} L'.format(altura,largura,tinta))

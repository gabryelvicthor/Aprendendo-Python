valor = float(input('Digite um valor em metros: '))
valorc = valor * 100
print('O valor digitado foi: {}\nO valor em centímetros é: {}\nO valor em milímetros é: {}'.format(valor,valorc, valorc * 10))
print('{} dm\n{} dam\n{} hm\n{} km'.format(valor * 10, valor / 10, valor / 100, valor /1000))
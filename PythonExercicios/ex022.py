nome = input('Digite seu nome completo: ')

print('Nome com letras maiúsculas: {}'.format(nome.upper()))
print('Nome com letras minúsculas: {}'.format(nome.lower()))

nomeModif = nome.split()
nomeJunto = ''.join(nomeModif)
print('Quantidade de letras: {}'.format(len(nomeJunto)))
print('Letras no primeiro nome: {}'.format(len(nomeModif[0])))
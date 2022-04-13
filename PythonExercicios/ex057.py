sexo = str(input('Digite seu sexo: ')).upper().strip()[0]

while sexo not in 'MmfF':
    sexo = str(input('Sexo errado, tente novamente. Digite seu sexo: ')).upper().strip()[0]

print('Sexo {} registrado com sucesso, parabéns'.format(sexo))
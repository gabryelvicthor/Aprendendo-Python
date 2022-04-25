nome = ''
idade = 0
sexo = 'F'
media = 0.0
velho = 0
nome_velho = ''
mulheres = 0
nova = 0

for i in range(1, 5):
    print('{:-^25}'.format(' {} ª PESSOA '.format(i) ))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    media += idade

    if sexo in 'Mm':
        if velho == 0:
            velho = idade
            nome_velho = nome
        elif velho < idade:
            velho = idade
            nome_velho = nome
    else:
        if nova < idade:
            nova = idade
        mulheres += 1
    
print('A média de idade do grupo é de {} anos'.format(media / 4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nome_velho))
print('Ao todo são {} mulheres com menos de {} anos.'.format(mulheres, nova))
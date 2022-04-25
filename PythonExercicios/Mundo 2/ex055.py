maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if maior == menor == 0:
        maior = peso
        menor = peso
    elif menor > peso:
        menor = peso
    elif maior < peso:
        maior = peso
        
print('O maior peso lido é: {:.2f} Kg'.format(maior))
print('O menor peso lido é: {:.2f} Kg'.format(menor))

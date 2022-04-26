maior = homens = mulheres = 0

while True:
    print('--' * 10)
    print('CADASTRE UMA PESSOA')
    print('--' * 10)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if idade < 20:
        if sexo == 'F':
            mulheres += 1

    if continuar == 'N':
        break

print(f'Total de pessoa com mais de 18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')

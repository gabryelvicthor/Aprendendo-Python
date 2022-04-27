print('--' * 20)
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print('--' * 20)
total = menor = caro = 0
while True:
    produto = str(input('Nome do produto: '))
    preço  = float(input('Preço: R$ '))
    total += preço
    if preço > 1000:
        caro += 1
    if menor == 0 or menor > preço:
        menor = preço
        produtoBarato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar != 'S':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {caro} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produtoBarato} que custa R$ {menor:.2f}')

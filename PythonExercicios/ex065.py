escolha = 'S'
maior = menor = media = quantidade = 0
while not escolha in 'Nn':
    num = int(input('Digite um número: '))
    escolha = str(input('Quer continuar? [S/N] ')).upper()
    quantidade += 1
    media += num
    if menor == 0 and maior == 0:
        menor = maior = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

media = media / quantidade
print('Você digitou {} números e a média foi {:.2f}'.format(quantidade,media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
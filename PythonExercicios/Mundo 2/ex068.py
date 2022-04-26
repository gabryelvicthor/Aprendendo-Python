from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)
cont = 0
while True:
    pc = randint(1, 10)
    valor = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar [P/I] ')).upper()
    soma = pc + valor
    print('--' * 15)
    if soma % 2 == 0:
        print(f'Você jogou {valor} e o computador {pc}. Total de {soma}, deu PAR')
        resultado = 'P'
    else:
        print(f'Você jogou {valor} e o computador {pc}. Total de {soma}, deu IMPAR')
        resultado = 'I'
    print('--' * 15)
    if escolha == resultado:
        print('Você GANHOU')
        print('Vamos jogar novamente...')
        print('=-' * 15)
        cont += 1
    else:
        print('Você PERDEU')
        print(f'GAME OVER! Você venceu {cont}ª vezes.')
        break

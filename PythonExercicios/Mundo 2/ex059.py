from time import sleep


laço1 = False

while not laço1:
    num1 = int(input('Primeiro número: '))
    num2 = int(input('Segundo valor: '))
    laço2 = False
    while not laço2:
        print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
        ''', end='')
        opção = int(input('Qual é a sua opção? '))
        if opção == 1:
            print('A soma entre {} + {} é {}'.format(num1, num2, num1 + num2))
        elif opção == 2:
            print('A multiplicação entre {} x {} é {}'.format(num1, num2, num1 * num2))
        elif opção == 3:
            if num1 > num2:
                maior = num1
            elif num1 < num2: 
                maior = num2
            else:
                maior = num1
            print('O maior número entre os escolhidos é: {} '. format(maior))
        elif opção == 4:
            laço2 = True
        elif opção == 5:
            print('Finalizando...')
            laço1 = True
            laço2 = True
        else:
            print('Opção inválida. Tente novamente.')
        sleep(1)
        print('-=-' * 10)
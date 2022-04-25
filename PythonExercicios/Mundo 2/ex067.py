cont = 1
while True:
    print('--' * 10)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('--' * 10)
    if n < 0:
        break
    while cont <= 10: 
        print(f'{n} x {cont} = {n * cont}')
        cont += 1
    cont = 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
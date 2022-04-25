import random
from time import sleep


print('-=-' * 19, '\nSou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
print('-=-' * 19)
cont = 0
acertou = False
numr = random.randint(1, 10)
while not acertou:
    num = int(input('Qual é o seu palpite? '))
    print('PROCESSANDO...') 
    sleep(1)
    cont += 1

    if num < numr:
        print('Mais... Tente mais uma vez.')
    elif num > numr:
        print('Menos... Tenta mais uma vez.')
    elif num == numr:
        print('Acertou na {}ª tentativa, pensei no número {}, Parabéns!'.format(cont, num))
        acertou = True

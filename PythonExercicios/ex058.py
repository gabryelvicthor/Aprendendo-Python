import random
from time import sleep


print('-=-' * 19)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 19)
cont = 0
num = -1
numr = random.randint(1, 10)
while numr != num:
    num = int(input('Em qual número eu pensei? '))
    print('PROCESSANDO...') 
    sleep(2)
    cont += 1

    if num == numr:
        print('Parabéns você acertou na {}ª tentativa, pensei no número {}'.format(cont, num))
    else:
        print('Errado! Não pensei no número {}. Tente novamente até acertar. '.format(num))

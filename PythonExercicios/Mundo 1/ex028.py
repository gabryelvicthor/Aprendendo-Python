import random
from time import sleep


print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)
num = int(input('Em qual número eu pensei? '))
numr = random.randint(1, 5)
print('PROCESSANDO...') 
sleep(2)

if num == numr:
    print('Parabens você acertou, pensei no número {}'.format(num))
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(numr, num))

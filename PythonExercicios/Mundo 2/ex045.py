import random
from time import sleep
print('''Suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA
''')

escolha = int(input('Qual é a sua jogada? '))
if escolha > 3 or escolha < 1:
    exit('{}Escolha incorreta, tente novamente{}'.format('\033[31m','\033[m'))
    

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)

escolhar = random.randint(1, 3)
itens = ('Pedra', 'Papel', 'Tesoura')

print('-=-' * 8)
print('Computador jogou {}'.format(itens[escolhar - 1]))
print('Jogador jogou {}'.format(itens[escolha -1]))
print('-=-' * 8)

if escolha == escolhar:
    resultado = 'Empate'
elif escolha == 1 and escolhar == 2:
    resultado = 'Computador Venceu'
elif escolha == 2 and escolhar == 1:
    resultado = 'Jogador Venceu'
elif escolha == 2 and escolhar == 3:
    resultado = 'Computador Venceu'
elif escolha == 3 and escolhar == 2:
    resultado = 'Jogador Venceu'
elif escolha == 1 and escolhar == 3:
    resultado = 'Jogador Venceu'
elif escolha == 3 and escolhar == 1:
    resultado = 'Computador Venceu'

print('{}'.format(resultado))

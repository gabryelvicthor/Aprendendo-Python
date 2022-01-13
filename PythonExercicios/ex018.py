import math

angulo = float(input('Digite um angulo qualquer: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O valor digitado foi: {}'.format(angulo))
print('O seno do valor é: {:.2f}'.format(seno))
print('O cosseno do valor é: {:.2f}'.format(cosseno))
print('A tangente do valor é: {:.2f}'.format(tangente))

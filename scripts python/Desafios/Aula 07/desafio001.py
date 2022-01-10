# potencia = pow(3,2)
# raiz = 9**(1/2)
# nome = input('Digite seu nome: ')

# print('Reesultado é: {}'.format(potencia))
# print('='*20)
# print('Reesultado é: {}'.format(raiz))

# print('{:=^20}'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
# print('A soma vale {}'.format(n1 + n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(' A soma é {}, \n O produto é {}, \n A divisão é {:.3f}\n'.format(s, m, d), end='>>>>>')
print('\n A Divisão inteira é {} \n A potência é {}'.format(di, e))

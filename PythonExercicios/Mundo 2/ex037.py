num = int(input('Digite um número inteiro: '))
cores = {'limpa':'\033[m',
        'verde':'\033[32m'}

print('[ 1 ] coverter para BINÁRIO ')
print('[ 2 ] coverter para OCTAL ')
print('[ 3 ] coverter para HEXADECIMAL ')
opcao = int(input('Sua opção: '))

if opcao == 1:

    print('O número {} em {}BINÁRIO{} é: {}'.format(num, cores['verde'], cores['limpa'], bin(num)[2:]))

elif opcao == 2:

    print('O número {} em {}OCTAL{} é: {}'.format(num, cores['verde'], cores['limpa'], oct(num)[2:]))

elif opcao == 3:

    print('O número {} em {}HEXADECIMAL{} é: {}'.format(num, cores['verde'], cores['limpa'], hex(num)[2:]))

else:
    print('Opção não existente, tentar novamente com a opção certa.')
    
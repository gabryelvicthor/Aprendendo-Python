nome = 'José'
idade = 33

print(f'O {nome} tem {idade} anos.') #PYTHON 3.6+
print('O {} tem {} anos.'.format(nome, idade)) #PYTHON 3
print('O %s tem %d anos.' % (nome, idade)) #PYTHON 2

salario = 566.45

print(f'O {nome:=^10} tem {idade:=^10} anos e ganha {salario:.2f}.')
preco = float(input('Digite o valo do produto: '))

cores = {'limpa':'\033[m', 
        'verde':'\033[32m', 
        'vermelho':'\033[31m'}

print('O novo valor com desconto de 5% é: {}{:.2f}{}'.format(cores['verde'],preco - (preco * 0.05), cores['limpa']))
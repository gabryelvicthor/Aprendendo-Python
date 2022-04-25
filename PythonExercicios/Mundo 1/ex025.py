nome = input('Qual é o seu nome completo? ').strip()

cores = {'limpa':'\033[m', 
        'verde':'\033[32m', 
        'vermelho':'\033[31m'}

print('Seu nome tem Silva? {}{}{}'.format(cores['vermelho'],'silva' in nome.lower(), cores['limpa']))
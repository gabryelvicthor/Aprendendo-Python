from distutils import core
import math
cOposto = float(input('Digite o cateto oposto do triângulo retângulo: '))
cAdjacente = float(input('Digite o cateto adjacente do triângulo retângulo: '))

cores = {'limpa':'\033[m', 
        'verde':'\033[32m', 
        'vermelho':'\033[31m'}
        
# hipotenuza = math.sqrt(math.pow(cOposto, 2) + math.pow(cAdjacente, 2))

hipotenuza = math.hypot(cOposto, cAdjacente)
print('A hipotenusa é igual a: {}{:.2f}{}'.format(cores['verde'],hipotenuza, cores['limpa']))

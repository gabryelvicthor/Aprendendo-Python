import math
cOposto = float(input('Digite o cateto oposto do triângulo retângulo: '))
cAdjacente = float(input('Digite o cateto adjacente do triângulo retângulo: '))
hipotenuza = math.sqrt(math.pow(cOposto, 2) + math.pow(cAdjacente, 2))
print('A hipotenusa é igual a: {:.2f}'.format(hipotenuza))

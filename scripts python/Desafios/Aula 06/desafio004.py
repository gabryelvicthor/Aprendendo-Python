algo = input('Digite algo: ')

print(type(algo))
print('É somente numeros:', algo.isnumeric())
print('É somente letras:', algo.isalpha())
print('É um alphanumerico:', algo.isalnum())
print('Está so com letras mainúsculas', algo.islower())
print('Está só com letras maiúsculas', algo.isupper())
print('Está capitalizada: ', algo.istitle())
print('Só tem espaços: ', algo.isspace())
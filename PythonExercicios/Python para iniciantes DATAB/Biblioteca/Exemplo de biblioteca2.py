import random

#Cria um inteiro aleatório dentro do range
aleatorio = random.randint(1, 10)
print(aleatorio)

#Cria um valor de ponto flutuante aleatório, utilizando o round pra limitar as casas decimais
pontoFlutuante = round(random.uniform(1, 5), 2)
print(pontoFlutuante)

#Escolhe um valor aleatorio dentro de uma lista
numeros = list(range(1,21))
print(numeros)
print("O valor escolhido aleatoriamente foi o: ", random.choice(numeros))

#Embaralha os valores de uma lista
print("A lista embaralhada:")
random.shuffle(numeros)
print(numeros)

#Pega dentro de uma lista uma certa quantidade de informações aleatoriamente.
print(random.sample(numeros, 5))

#Retorna os valores inteiros do intervalo, utilizando o 3 parametro para o intervalo entreos números
print(random.randrange(0, 51, 2))
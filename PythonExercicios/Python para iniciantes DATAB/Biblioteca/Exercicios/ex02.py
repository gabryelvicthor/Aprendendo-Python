#Faça um programa que gere seis números da megasena de forma aleatória( os números devem ser entre
# 1 e 60). Armazene os em uma lista e imprima na tela.# 
import random

#Criando um for prara gerar os números aleatórios

lista = []

for i in range(1, 7):
    lista.append(random.randint(1, 60))

print(lista)
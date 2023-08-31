#Faça um programa que tenha um dicionário que contenha todas as suas informações(nome, sexo, idade 
# e altura) e imprima esses valores através de um laço for#

pessoa = {
    "nome": "Gabryel",
    "idade": 23,
    "peso": 85,
    "sexo": "masculino",
    "cnh": "AB",
    "altura": 1.89
} 

for index, valor in pessoa.items():
    print("{}: {}".format(index, valor))
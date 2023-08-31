#Preecha dois dicionários contendo quaisquer informações e faça a atualização de um deles com base
# no outro dicionário. Imprima o antes e o depois na tela.#


pessoa1 = {
    "nome": "Gabryel",
    "idade": 23,
} 

print(pessoa1)

pessoa2 = {
    "peso": 85,
    "sexo": "masculino",
    "cnh": "AB",
    "altura": 1.89
} 

print(pessoa2)

pessoa1.update(pessoa2)

print(pessoa1)
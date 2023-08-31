#Um dicionario é criado usando {}, e os seus valores são o index e o valor do mesmo, que 
# podem ser escolhidos.#

pessoa = {
    "nome": "Gabryel",
    "idade": 23,
    "peso": 85
} 

print("{}, {}".format(pessoa, type(pessoa)))

pessoa["nome"] = "Lohran"
pessoa["idade"] = 22
print(pessoa)
print("--" * 40)

#del é utilizado pra apagar um indice de um dicionario.
# popitem é utilizado para apagar o ultimo indice adicionado.
# .pop é usado para apagar um indice pelo seu nome
# clear = limpa todos as informações do dicionário#

pessoa2 = {
    "nome": "Gabryel",
    "idade": 23,
    "peso": 85,
    "sexo": "masculino",
    "cnh": "AB",
    "altura": 1.89
} 

print(pessoa2)
del pessoa2["peso"]
print(pessoa2)
pessoa2.popitem()
print(pessoa2)
pessoa2.pop("idade")
print(pessoa2)
pessoa2.clear()
print(pessoa2)

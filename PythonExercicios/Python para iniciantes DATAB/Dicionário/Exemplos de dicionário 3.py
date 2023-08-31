# metodo keys, values e itens são para ver os itens dentro do dicionário, keys para as chaves,
# values para os valores e items para os 2 valores.

pessoa = {
    "nome": "Gabryel",
    "idade": 23,
    "peso": 85,
    "sexo": "masculino",
    "cnh": "AB",
    "altura": 1.89
} 

for indice, valor in pessoa.items():
    print("Indice: {} \nValor: {}".format(indice, valor))
    print("--"*20)

#.updata() = Função que serve para incerir novos valores ou atualizar valores do dicionario.

pessoaNovo = {
    "cpf": "235.123.654-25"
}

pessoa.update(pessoaNovo)
pessoa.update(cabeloCor = "preto")

print(pessoa)
#Métodos get e copy: get puxa o valor que está contino no index, e caso não encontre há um
#segundo parametro que pode ser exibido nesse caso.
# O copy faz uma referência(mesmo se mudar algum valor o novo continua referenciando) do dicionáio
#  em outro dicionario#

pessoa = {
    "nome": "Gabryel",
    "idade": 23,
    "peso": 85,
    "sexo": "masculino",
    "cnh": "AB",
    "altura": 1.89
} 

print(pessoa.get("nome"))
pessoa.pop("nome")
print(pessoa.get("nome"))
print(pessoa.get("nome","Valor não encontrado"))

pessoaCopia = pessoa.copy()
print(pessoa)
print(pessoaCopia)
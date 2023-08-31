#Dado o dicionário do exercicio 04, verifique se o número "seis" e o "onze" estão
# contidos nele. O resultado deverá ser impresso na tela sendo True ou False para
# cada caso.#

pessoa1 = {
    "nome": "Gabryel",
    "idade": 23,
} 


pessoa2 = {
    "peso": 85,
    "sexo": "masculino",
    "cnh": "AB",
    "altura": 1.89
} 


if pessoa1.get("seis") != None:
    print("True")
else:
    print("False")

if pessoa1.get("onze") != None:
    print("True")
else:
    print("False")

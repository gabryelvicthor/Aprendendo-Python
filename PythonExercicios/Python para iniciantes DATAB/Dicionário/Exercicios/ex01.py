#Crie um dicionário qe contenha todos os dias da semana, após isso, utilize algum método para 
# remover os dias do final de semana.#

diaSemana = {
    1: "Segunda-feira",
    2: "Terça-feira",
    3: "Quarta-feira",
    4: "Quinta-feira",
    5: "sexta-feira",
    6: "Sabado",
    7: "Domingo"
}

diaSemana.pop(6)
diaSemana.pop(7)
print(diaSemana)
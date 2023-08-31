#Através de algum dicionário criado por você nos exercicios anteriores, você
# deverá remover o último valor desse dicionário, remover um valor informando a sua
# respectiva chave e após isso limpar todo o dicionário.
# Dica: serão usados 3 métodos distintos.#

diaSemana = {
    1: "Segunda-feira",
    2: "Terça-feira",
    3: "Quarta-feira",
    4: "Quinta-feira",
    5: "sexta-feira",
    6: "Sabado",
    7: "Domingo"
}

diaSemana.popitem()
diaSemana.pop(3)
print(diaSemana)
diaSemana.clear()
print(diaSemana)
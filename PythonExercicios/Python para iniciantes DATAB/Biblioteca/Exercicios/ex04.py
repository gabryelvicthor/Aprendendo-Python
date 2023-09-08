#Faça um programa dinâmico que imprima na tela qual é o dia da semana que você se encontra#

from datetime import date


diaSemana = date.today().weekday()
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sabado", "Domingo"]

print("Hoje é {}".format(semana[diaSemana]))
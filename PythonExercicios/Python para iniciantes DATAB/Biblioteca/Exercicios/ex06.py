#Faça um programa que receba o ano em que você nasceu e o ano em que você deseja saber a sua idade.
# Faça o cálculo necessário e mostre sua idade na tela de acordo com os anos inseridos#
#Vou fazer de acordo com o ano atual#

from datetime import date


anoNasc = 0
anoAtual = date.today().year

#Recebendo os valores
anoNasc = int(input("Digite o ano em que você nasceu: "))

#Fazendo o calculo
idade = anoAtual - anoNasc

print("Sua idade nesse ano é: {}".format(idade))

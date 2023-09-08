# Faça um programa que receba a data de aniversário do usuário e calcule quantos dias faltam para seu próximo aniversário ( considerando a data atual da execução do código)#

#Coletando dados
from datetime import date


ano = 0
dia = int(input("Digite o dia do seu aniversário: "))
mes = int(input("Digite o mês do seu aniversário: "))

#Calculando
if mes >= date.today().month:
    #Aniversário ainda não chego
    ano = date.today().year
else:
    #Aniversário já passou
    ano = date.today().year + 1

aniversario = date(ano, mes, dia)
hoje = date.today()
diferenca = aniversario - hoje

if diferenca.days != 0:
    print("Faltam {} dias para o seu aniversário.".format(diferenca.days))
else:
    print("Parabéns hoje é o seu aniversário!!")
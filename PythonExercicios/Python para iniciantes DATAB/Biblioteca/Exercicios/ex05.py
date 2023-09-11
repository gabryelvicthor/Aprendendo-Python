#Faça um programa que receba 5 números aleatórios em uma lista e imprima-os na tela de forma ordenada
# e também na forma desordenada#

lista = []

#Recebendo os valores
for i in range(1, 6):
    lista.insert(i, int(input("Digite o {}° número: ".format(i))))

#Mostrando os valores ordenados e desordenados
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
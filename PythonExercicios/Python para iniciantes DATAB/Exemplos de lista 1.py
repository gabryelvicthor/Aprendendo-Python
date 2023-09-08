from pickle import APPEND

#append = Adiciona ao final de um lista um dado qualquer.
#index = indica a posição de um elemento na lista (.index(3))
#insert and remove = O primeiro insere na lista em um index específico e o outro
# remove o elemento que é especificado e encontrado primeiro.

lista = []
valor = 0

for i in range(0, 4):
    valor = int(input("Digite um número: "))
    lista.append(valor)

print(lista)

lista.insert(0, "Primeiro")
lista.insert(5, "Ultimo")
print(lista)
lista.remove("Primeiro")
print(lista)

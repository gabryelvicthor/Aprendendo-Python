
#count = Faz a contagem do elemento na lista.

lista = [1, 2, 43, 2, 1, 1, 3, 4, 1, 2, 1]
print(lista.count(1))

#sort() = faz a ordenação dos elementos em ordem alfabetica, podendo ser adicionado nos parametros
# o (reverse = true) assim ordenando reversamente#

lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#.pop() é um modo de remover itens da lista pelo seu indice.

lista.pop(2)
lista.pop(0)
print(lista)
lista.append(4)
print(lista)
lista.remove(4)
print(lista)
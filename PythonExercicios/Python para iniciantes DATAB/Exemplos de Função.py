#sum() = Faz a soma de todos os indices dentro de uma lista.
#max() e min() = encontra o número com o maior valor e o menor dentro de uma lista.
#round = arredonda valores, podendo ter um segundo parametro que escolhe a quantidade 
# de casas decimais a serem arredondadas.#

x = 13.5674
print(round(x))
print(round(x, 2))

#range(1, 20, 2) é uma função usada pra criar uma lista de valores onde o primeiro argumento é 
# o número inicial, os segundo é o final e o terceiro é o intervalo. podendo ser utilizado somente 
# um argumento que se iniciaria no 0 e iria ate o número - 1#
#len(y) = faz a conta de quando elementos há em uma lista ou em um nome ou frase( Contando os espaços).

y = "Amor não é ruim"
print(len(y))

#enumerate(nome) = cria indices para cada elemento de uma lista na hora de ser mostrado na tela

nome = ["Gabryel", "Lohran", "Marcus", "Vinicios"]
for n in enumerate(nome):
    print(n)
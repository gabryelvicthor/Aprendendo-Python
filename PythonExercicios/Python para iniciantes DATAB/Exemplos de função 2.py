#Exemplos de criação de funções#

#Função que multiplica valores dentro de uma lista
def mult(numeros):
    resultado = 1
    for x in numeros:
        resultado *= x
    return resultado

#Função que verifica se um número está dentro de um intervalo definido
def verif(numero, min, max):
    if numero in range(min, max + 1):
        print("O número {} está DENTRO do intervalo {} e {}".format(numero, min, max))
    else:
        print("O número {} está FORA do intervalo {} e {}".format(numero, min, max))

#Função que pega uma lista e tira os repetidos
def exclusivo(lista):
    valores = []
    for iteracoes in lista:
        if iteracoes not in valores:
            valores.append(iteracoes)
    return valores

teste1 = [3,4,10]
print(mult(teste1))

verif(20, 10, 20)

teste3 = [1, 2, 3, 1, 2, 1, 1 , 3, 7, 8, 9, 9, 12, 3, 5, 2, 1]
print(exclusivo(teste3))
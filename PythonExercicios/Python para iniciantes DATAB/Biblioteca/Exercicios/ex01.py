#Utilizando uma biblioteca e a funcção dequada, realize a segunte operação:
# A = n! / (n - k)
# a onde o usuário deverá inserir os valores para as variáveis da expressão.#
import math

#Pegando as informações
print("Para fazer o calculo A = n! / (n - k) digite as variáveis a seguir:")
n = int(input("n: "))
k = int(input("k: "))

#fazendo o calculo
nF = math.factorial(n)
resposta = nF / (n - k)

#Resposta
print("--" * 20)
print("A resposta é: {:.2f}".format(resposta))
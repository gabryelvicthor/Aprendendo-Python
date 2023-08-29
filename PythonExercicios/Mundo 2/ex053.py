frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

# inverso = junto[::-1] >>> Usando fatiamento
 
for letras in range(len(junto) -1, -1, -1):
    inverso += junto[letras]

print('O inverso de "{}" é: {}'.format(frase, inverso))

if junto == inverso:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')



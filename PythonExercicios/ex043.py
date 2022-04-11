from math import pow

peso = float(input('Qual é o seu peso? (kg): '))
altura = float(input('Qual é a sua altura? (m): '))

#A elevação por 2 pode ser feita assim também (altura ** 2)
imc = peso / pow(altura, 2)

print('O seu IMC é de {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Parabéns, você está na faixa de peso ideal.')
elif imc < 30:
    print('Você está na faixa de sobrepeso')
elif imc < 40:
    print('Você está na faixa de obesidade')
elif imc >= 40:
    print('Você está na faixa de obesidade mórbida, cuidado!!')
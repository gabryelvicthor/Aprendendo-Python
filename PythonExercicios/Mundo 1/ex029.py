vel = float(input('Qual é a velociodade atual do carro? '))
if vel > 80:
    print('Multado! Você excedeu o limite permitido que é de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format((vel - 80) * 7))

print('Tenha um bom dia! Dirija com segurança!')
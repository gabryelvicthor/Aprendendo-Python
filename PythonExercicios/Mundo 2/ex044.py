#print('==' * 5, end = '')
#print('LOJAS GABRYEL', end = '')
#print('==' * 5)
# ou 
# print('{:=^40}'.format(' LOJAS GABRYEL '))
# Centralizado em 40 espaços com '=' preenchendo os espaços em branco

print('==' * 5 + ' LOJAS GABRYEL ' + '==' * 5)
preço = float(input('Prço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

desc_dinheiro = preço * 0.10
desc_cartão = preço * 0.05
juros = preço * 0.20

opção = int(input('Qual é a opção? '))

if opção == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, preço - desc_dinheiro))
elif opção	== 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, preço - desc_cartão))
elif opção	== 3:
   print('Sua compra será parcelada em 2x de R${:.2f} sem Juros'.format(preço / 2))
elif opção	== 4:
    parcelas = int(input('Quantas parcelas?'))

    print('Sua compra será parcelada em {:.0f}x de R${:.2f} com Juros'.format(parcelas, (preço + juros) / parcelas))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, preço + juros ))

else:
    print('{}Opção inválida, tente novamente.{}'.format('\033[31m','\033[m' ))
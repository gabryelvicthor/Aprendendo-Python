from datetime import date

maiores = 0
menores = 0
ano = date.today().year

for i in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    idade = ano - nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
print('E também tivemos {} pessoas menores de idade'.format(menores))

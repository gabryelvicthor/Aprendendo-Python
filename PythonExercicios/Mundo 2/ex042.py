n1 = float(input('Primeiro seguimento: '))
n2 = float(input('Segundo seguimento: '))
n3 = float(input('Terceiro seguimento: '))

#, end=''
#Junta o print de baixo com o de cima.

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    forma = 'Podem formar'

    if n1 == n2 == n3:
        tipo = ' Equilátero'
    elif n1 != n2 != n3 != n1:
        tipo = ' Escaleno'
    else:
        tipo = ' Isóceles'
else: 
    forma = 'Não forma'
    tipo = ''

print('Os seguimento acima {} um triângulo{}! '.format(forma, tipo))
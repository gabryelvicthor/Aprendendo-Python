from typing import final


while True:
    try:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        divisao = n1/n2
        print("A divisão entre {} e {} é igual a {}".format(n1, n2, divisao))
    
    except ZeroDivisionError:
        print("Não é possível fazer divisão por zero.")
    except ValueError:
        print("Apenas números são aceitos")
    except TypeError:
        print("A variavel tem q ser inteira.")

    continuar = ' '
    while continuar not in "sn":
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar != "s":
        break

print("Programa Finalizado!")

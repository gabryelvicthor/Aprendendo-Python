while True:
    try:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
        divisao = n1/n2
        print("A divisão entre {} e {} é igual a {}".format(n1, n2, divisao))

        continuar = ' '
        while continuar not in "SN":
            continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar != "S":
            break
    except ZeroDivisionError:
        print("Não é possível fazer divisão por zero.")
    except ValueError:
        print("Apenas números são aceitos")
    except TypeError:
        print("A variavel tem q ser inteira.")

print("Programa Finalizado!")

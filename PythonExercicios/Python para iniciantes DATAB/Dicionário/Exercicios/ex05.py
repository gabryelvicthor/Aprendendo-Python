#Atravéz do dicionário abaixo:
# números ={
#   1: "um",
#   2: "dois",
#   3: "três",
#   4: "quatro",
#   5: "cinco",
#   6: "seis",
#   7: "sete",
#   8: "oito",
#   9: "nove",
#   10: "dez"
# }

numeros ={
   1: "um",
   2: "dois",
   3: "três",
   4: "quatro",
   5: "cinco",
   6: "seis",
   7: "sete",
   8: "oito",
   9: "nove",
   10: "dez"
 }

print("Chaves:")
print("--"*20)
for i in numeros.keys():
    print(i)

print("--"*20)
print("Valores:")
print("--"*20)
for i in numeros.values():
    print(i)

print("--"*20)
print("Dicionário:")
print("--"*20)
for i, j in numeros.items():
    print("{}: {}".format(i, j))
print("--"*20)
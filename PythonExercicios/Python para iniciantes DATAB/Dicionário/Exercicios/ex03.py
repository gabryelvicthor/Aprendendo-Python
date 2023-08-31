#Faça um programa que receba em um dicionário as seguntes informações de uma empresa: razão social,
# CNPJ e proprietário, e mostre todos os valores na tela (ao mostrar os valores captados na tela,
# utilize o método responsável para evitar erros ao buscar valores inexistentes em um dicionário e
# teste essa funcionalidade.#

empresa = {
    "rs": "",
    "cnpj": "",
    "prop": ""
}

print("Digite as informações da empresa:")
print("__"*20)
empresa.update(rs = str(input("Razão Social: ")))
empresa.update(cnpj = str(input("CNPJ: ")))
empresa.update(prop = str(input("Proprietário: ")))
print("__"*20)

for i in empresa.values():
    print(i)
print("__"*20)

print("Escolha um dado para ver novamente: " +
"\nRazão social: 1" +
"\nCNPJ: 2" +
"\nProprietário: 3")
print("__"*20)

escolha = int(input(": "))

if escolha == 1:
    v = "sr"
elif escolha == 2:
    v = "cnpj"
else:
    v = "prop"

print(empresa.get(v, "Número desconhecido"))

linhas = int(input("Insira o numero de linhas: "))
colunas = int(input("Insira o numero de colunas: "))
simbolos = input("Insira um simbolo para usar: ")

for x in range (linhas):
    for y in range(colunas):
        print(simbolos, end="")
    print() 
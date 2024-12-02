idade = int(input("Insira sua idade: "))

while idade <= 0:
    print("Essa idade não pode ser zero ou negativa")
    idade = int(input("Insira sua idade: "))
print(f"Sua idade é {idade} anos")
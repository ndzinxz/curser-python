numero = int(input("Insira um número entre 1 - 10: "))

while numero < 1 or numero > 10:
    print(f"{numero} não é válido")
    numero = int(input("Insira um número entre 1 - 10: "))

print(f"Seu número é {numero}")
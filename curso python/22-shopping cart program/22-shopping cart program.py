# shopping cart program

comidas = []
preços = []
total = 0

while True:
    comida = input("Insira uma comida para comprar (q para sair): ")
    if comida.lower() == "q":
        break
    else:
        preço = float(input(f"Insira o preço do(a) {comida} : R$"))
        comidas.append(comida)
        preços.append(preço)

print("----- SEU CARRINHO -----")

for comida in comidas:
    print(comida, end=" ")

for preços in preços:
    total += preço

print()
print(f"Seu total é: R${total}")
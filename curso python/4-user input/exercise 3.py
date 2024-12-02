item = input("Qual item você deseja comprar?: ")
preço = float(input("Qual preço você gostaria de pagar?: "))
quantidade = int(input("Quantos (a) você deseja levar?: "))

total = preço * quantidade

print(f"Você comprou {quantidade} x {item}/s")
print(f"Sua compra total foi: R${total}")
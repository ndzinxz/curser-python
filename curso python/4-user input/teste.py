# teste compras com desconto


item = input("Qual item você deseja comprar?: ")
preço = float(input("Qual é o valor?:"))

desconto = preço - (preço * 0.10) 
aumento = preço * 0.10

print(f"o preço do(a) {item} com o desconto é {desconto}$")
print(f"o preço do(a) {item} com o a taxa de imposto foi de {aumento}$")
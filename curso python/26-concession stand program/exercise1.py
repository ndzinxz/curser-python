mercado = {"arroz": 5.00,
           "feijao": 6.00,
           "macarrão": 7.00,
           "farinha": 8.00,
           "alface": 9.00,
           "cenoura": 10.00,
           "brocolis": 11.00,
           "espinafre": 12.00,
           "frango": 13.00,
           "picanha": 14.00,
           "costela": 15.00,
           "alcatra": 16.00,
           }
carrinho = []
total = 0

print("-" * 15, "MERCADO", "_" * 15)

for key, value in mercado.items():
    print(f"{key:13}: R${value:.2f}")
print("-" * 37)

while True:
    menu = input("Selecione os itens do mercado (q para encerrar a compra): ")
    if menu == "q":
        break
    elif mercado.get(menu) is not None:
        carrinho.append(menu)

print("-" * 15, "CARRINHO", "_" * 15)
for menu in carrinho:
    total += mercado[menu]
    print(menu, end=" ")

print()
print(f"Seu total é: R${total:.2f}")

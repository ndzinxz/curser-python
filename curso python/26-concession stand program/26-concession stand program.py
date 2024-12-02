# Programa de estandes de concessão

menu = {"pizza": 3.00,
        "hamburguer": 4.00,
        "sorvete": 2.00,
        "hamburguer": 4.00,
        "sorvete": 2.00,
        "refri": 1.50,
        "suco": 1.80,
        "refri": 1.50,
        "suco": 1.80,
        "fritas": 2.00,
        "coxinha": 3.50,
        "empada": 5.00,
        }
carrinho = []
total = 0

print("-" * 10, "MENU", "-" * 10)

for chave, valor in menu.items():
    print(f"{chave:11}: R${valor:.2f}")
print("-" * 26)

while True:
    comida = input("Selecione o item do menu (q para sair)")
    if comida == "q":
        break
    elif menu.get(comida) is not None:
        carrinho.append(comida)

print("-" * 10, "SEU PEDIDO", "-" * 10)
for comida in carrinho:
    total += menu.get(comida)
    print(comida, end=" ")

print()
print(f"Total é: R${total:.2f}")

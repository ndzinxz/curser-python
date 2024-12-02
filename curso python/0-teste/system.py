# Definindo os produtos e preços
itens = {
    "Arroz": 5.00,
    "Feijao": 6.00,
    "Macarrão": 7.00,
    "Farinha": 8.00,
    "Alface": 9.00,
    "Cenoura": 10.00,
    "Brocolis": 11.00,
    "Espinafre": 12.00,
    "Frango": 13.00,
    "Picanha": 14.00,
    "Costela": 15.00,
    "Alcatra": 16.00,
}

# Variável para acumular o total da compra
total_compra = 0.0

# Loop para receber o item e quantidade do usuário
while True:
    print("\nProdutos disponíveis:")
    for item, preco in itens.items():
        print(f"{item} - R${preco:.2f}")

    # Entrada do item desejado
    item = input("\nQual item você deseja comprar? (q para finalizar a compra): ").capitalize()

    if item.lower() == "q":
        print("Compra finalizada.")
        break

    if item not in itens:
        print("Produto inválido")
        continue

    # Solicitar a quantidade
    try:
        quantidade = int(input("Quantas unidades você deseja comprar?: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue

    # Determinando o preço e calculando o total do item
    preco = itens[item]
    total_item = preco * quantidade
    total_compra += total_item  # Acumula o total da compra

    # Exibindo o total do item
print(f"\nVocê comprou {quantidade} x {item}(s) - Total: R${total_item:.2f}")

# Exibindo o total final da compra
print(f"\nO valor total da sua compra é: R${total_compra:.2f}")

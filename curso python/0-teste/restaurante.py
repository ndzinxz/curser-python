#Restaurante - python

#pratos
prato1 = "Prato 1: Arroz, Feijão, Farofa e Bife"
prato2 = "Prato 2: Arroz, Feijão, Farofa e Frango"
prato3 = "Prato 3: Arroz, Feijão, Farofa e Churrasco misto"
prato4 = "Prato 4: Arroz, Feijão, Farofa e Peixe"
prato5 = "Prato 5: Arroz, Feijão, Farofa e Ovo"

#preço
p1 = 15.00
p2 = 17.00
p3 = 25.00
p4 = 20.00
p5 = 12.00

produtos = input(f"{prato1} R$ {p1}\n{prato2} R$ {p2}\n{prato3} R$ {p3}\n{prato4} R$ {p4}\n{prato5} R$ {p5}\nEscolha o prato: ")

while not produtos in ["Prato 1", "Prato 2", "Prato 3", "Prato 4", "Prato 5"]:
    print("Prato inválido")
    produtos = input(f"{prato1} R$ {p1}\n{prato2} R$ {p2}\n{prato3} R$ {p3}\n{prato4} R$ {p4}\n{prato5} R$ {p5}\nEscolha o prato: ")

if produtos == "Prato 1":
    print("Você escolheu o Prato1.")
    quantidade = int(input("Quantas você deseja levar?: "))
    total = p1 * quantidade
    print("----------------------------------------")
    print(f"Você comprou {quantidade} x {prato1}")
    print(f"Sua compra total foi: R$ {total}")

elif produtos == "Prato 2":
    print("Você escolheu o Prato2.")
    quantidade = int(input("Quantas você deseja levar?: "))
    total = p2 * quantidade
    print("----------------------------------------")
    print(f"Você comprou {quantidade} x {prato2}")
    print(f"Sua conta total foi: R$ {total}")

elif produtos == "Prato 3":
    print("Você escolheu o Prato3.")
    quantidade = int(input("Quantas você deseja levar?: "))
    total = p3 * quantidade
    print("----------------------------------------")
    print(f"Você comprou {quantidade} x {prato3}")
    print(f"Sua conta total foi: R$ {total}")

elif produtos == "Prato 4":
    print("Você escolheu o Prato4.")
    quantidade = int(input("Quantas você deseja levar?: "))
    total = p4 * quantidade
    print("----------------------------------------")
    print(f"Você comprou {quantidade} x {prato4}")
    print(f"Sua conta total foi: R$ {total}")

elif produtos == "Prato 5":
    print("Você escolheu o Prato5.")
    quantidade = int(input("Quantas você deseja levar?: "))
    total = p5 * quantidade
    print("----------------------------------------")
    print(f"Você comprou {quantidade} x {prato5}")
    print(f"Sua conta total foi: R$ {total}")


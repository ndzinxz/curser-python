# Python weight conversion

peso = float(input("Insira seu peso: "))
unidade = input("Kilogramas ou libras? (kg ou lb): ")

if unidade == "kg":
    peso = peso * 2.205
    unidade = "lb."
elif unidade == "lb":
    peso = peso / 2.205
    unidade = "kg."
    print(f"Seu peso é: {round(peso, 1)} {unidade}")
else:
    print(f"{unidade} não é valido")
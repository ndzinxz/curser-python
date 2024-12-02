comida = input("Insira uma comida que você gosta (q para desistir): ")

while not comida == "q":
    print(f"Você gosta de {comida}")
    comida = input("Insira outra comida que você gosta (q para desistir): ")

print("bye")
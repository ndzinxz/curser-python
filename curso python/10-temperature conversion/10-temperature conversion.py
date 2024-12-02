unidade = input("Essa temperatura está em Celsius ou Fahrenheit (C/F): ")
tempo = float(input("Insira a temperatura: "))

if unidade == "C":
    tempo = round((9 * tempo) / 5 + 32, 1)
    print(f"A temperatura em Fahrenheit é: {tempo}ºF")

elif unidade == "F":
    tempo = round((tempo - 32) * 5 / 9, 1)
    print(f"A temperatura em Celsius é: {tempo}ºC")

else:
    print(f"{unidade} é uma unidade de medida inválida")
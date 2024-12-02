import random

opcoes = ("pedra", "papel", "tesoura")
jogador = None
computador = random.choice(opcoes)

while jogador not in opcoes:
    jogador = input("Escolha (pedra, papel ou tesoura): ")

print(f"jogaor: {jogador}")
print(f"computador: {computador}")

if jogador == computador:
    print("Empate")
elif jogador == "pedra" and computador == "tesoura":
    print("Você ganhou!")
elif jogador == "papel" and computador == "pedra":
    print("Você ganhou!")
elif jogador == "tesoura" and computador == "papel":
    print("Você ganhou!")
else:
    print("Você perdeu!")

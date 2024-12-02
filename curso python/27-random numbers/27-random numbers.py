import random

baixo = 1
alto = 50
opcoes = ("pedra", "papel", "tesoura")
cartoes = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# numero = random.randint(baixo, alto)
# numero = random.random()
# opcao = random.choice(opcoes)
random.shuffle(cartoes)

print(cartoes)

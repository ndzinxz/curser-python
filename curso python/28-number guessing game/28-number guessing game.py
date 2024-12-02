import random

numero_mais_baixo = 1
numero_mais_alto = 100
resposta = random.randint(numero_mais_baixo, numero_mais_alto)
suposicoes = 0
esta_correndo = True

print("jogo de adivinhação de números python")
print(f"selecione um número entre {numero_mais_baixo} e {numero_mais_alto}")

while esta_correndo:

    suposicao = input("digite seu palpite: ")

    if suposicao.isdigit():
        suposicao = int(suposicao)
        suposicao += 1

        if suposicao < numero_mais_baixo or suposicao > numero_mais_alto:
            print("Esse número está fora do alcance")
            print(
                f"Por favor, selecione um número entre {numero_mais_baixo}"
                f"e {numero_mais_alto}.")
        elif suposicao < resposta:
            print("Seu palpite foi muito baixo")
        elif suposicao > resposta:
            print("Seu palpite foi muito alto")
        else:
            print(f"CORRETO! A resposta foi {resposta}")
            print(f"Número de palpites: {suposicao}")
            esta_correndo = False
    else:
        print("estimativa invalida")
        print(
            f"Por favor, selecione um número entre {numero_mais_baixo} e "
            f"{numero_mais_alto}."
        )

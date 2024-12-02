# python quiz game

questoes = ("Quantos elementos existem na tabela periódica?",
            "Qual animal põe os maiores ovos?",
            "Qual é o gás mais abundante na atmosfera da Terra?",
            "Quantos ossos há no corpo humano?",
            "Qual planeta do sistema solar é o mais quente?")

opcoes = (("(A) 102", "(B) 108", "(C) 118", "(D) 126"),
          ("(A) Avestruz", "(B) Pato", "(C) Águia", "(D) Pinguin"),
          ("(A) Oxigênio", "(B) Hidrogênio", "(C) Nitrogênio",
           "(D) Díoxido de Carbono"),
          ("(A) 196", "(B) 206", "(C) 216", "(D) 226"),
          ("(A) Mercúrio", "(B) Vênus", "(C) Marte", "(D) Júpiter"))

respostas = ("C", "A", "C", "B", "B")
suposicoes = []
pontuacao = 0
questao_num = 0

for questao in questoes:
    print("----------------------------------")
    print(questao)
    for opcao in opcoes[questao_num]:
        print(opcao)

    suposicao = input("Escolha uma opção (A, B, C ou D): ").upper()
    suposicoes.append(suposicao)
    if suposicao == respostas[questao_num]:
        pontuacao += 1
        print("Resposta correta!")
    else:
        print("Resposta errada!")
        print(f"A resposta correta era: {respostas[questao_num]}")
    questao_num += 1

print("----------------------------------")
print("             RESULTADO            ")
print("----------------------------------")
print("Obrigado por participar do jogo!")
print(f"Sua pontuação foi: {pontuacao}/5")
print("Respostas: ", end="")
for resposta in respostas:
    print(resposta, end=" ")
print()

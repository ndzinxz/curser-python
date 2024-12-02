principio = 0
taxa = 0
tempo = 0

while True:
    principio = float(input("Insira o principal valor: "))
    if principio <= 0:
        print("principio não pode ser menor ou igual a zero")
    else:
        break

while True:
    taxa = float(input("Insira a taxa: "))
    if taxa <= 0:
        print("taxa não pode ser menor ou igual a zero")
    else:
        break

while True:
    tempo = int(input("Insira o tempo em anos: "))
    if tempo <= 0:
        print("tempo não pode ser menor ou igual a zero")
    else:
        break

total = (principio * (1 + (taxa / 100)) ** tempo)
print(f"o quilibrio após {tempo} anos é de: ${total:.2f}")
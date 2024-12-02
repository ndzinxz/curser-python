# or

#tempo = 20
#chovendo = False
#
#if tempo > 35 or tempo < 0 or chovendo:
#    print("O evento ao ar livre foi cancelado")
#
#else:
#    print("o evento ao ar livre ainda está #agendado")

# and

tempo = 25
sol = True

if tempo >= 28 and sol:
    print("Está quente lá fora")
    print("Está ensolarado")

elif tempo <= 0 and sol:
    print("Está frio lá fora")
    print("Está ensolarado")

elif 28 > tempo > 0 and sol:
    print("Está esquentando lá fora")
    print("Está ensolarado")

elif tempo >= 28 and not sol:
    print("Está quente lá fora")
    print("Está ensolarado")

elif tempo <= 0 and not sol:
    print("Está frio lá fora")
    print("Está ensolarado")

elif 28 > tempo > 0 and not sol:
    print("Está esquentando lá fora")
    print("Está ensolarado")
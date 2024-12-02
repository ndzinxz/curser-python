idade = int(input("Insira sua idade: "))

if idade >= 18:
    print("Agora você está inscrito!")

elif idade < 0:
    print("Você ainda não nasceu!")

else:
    print("Você precisa ser maior de 18 anos para se inscrever")
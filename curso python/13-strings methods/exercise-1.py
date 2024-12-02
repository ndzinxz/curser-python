nome_usuario = input("Insira seu nome de usuário: ")

nome_usuario.find(" ")

if len(nome_usuario) > 12:
    print("Seu nome de usuário não pode ter mais de 12 caracteres")
elif not nome_usuario.find(" ") == -1:
    print("Seu nome de usuário não pode conter espaço")
elif not nome_usuario.isalpha():
    print("Seu nome de usuário não pode conter números")
else:
    print(f"Bem vindo {nome_usuario}")
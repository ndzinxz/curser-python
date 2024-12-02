# Python calculator / concatenação

operador = input("Insira um operador (+ - * /): ")
num1 = input("Insira o 1º número: ")
num2 = input("Insira o 2º número: ")
print(num1 + num2)


operador = input("Insira um operador (+ - * /): ")
num1 = float(input("Insira o 1º número: "))
num2 = float(input("Insira o 2º número: "))
print(num1 + num2)


# Operação de acordo com o sinal

operador = input("Insira um operador (+ - * /): ")
num1 = float(input("Insira o 1º número: "))
num2 = float(input("Insira o 2º número: "))

if operador == "+":
    resultado = num1 + num2
    print(resultado)

elif operador == "-":
    resultado = num1 - num2
    print(resultado)

elif operador == "*":
    resultado = num1 * num2
    print(resultado)

elif operador == "/":
    resultado = num1 / num2
    print(resultado)


# Arredondar para o numero mais proximo

operador = input("Insira um operador (+ - * /): ")
num1 = float(input("Insira o 1º número: "))
num2 = float(input("Insira o 2º número: "))

if operador == "+":
    resultado = num1 + num2
    print(round(resultado))

elif operador == "-":
    resultado = num1 - num2
    print(round(resultado))

elif operador == "*":
    resultado = num1 * num2
    print(round(resultado))

elif operador == "/":
    resultado = num1 / num2
    print(round(resultado))


# números após a virgula (DECIMAIS)

operador = input("Insira um operador (+ - * /): ")
num1 = float(input("Insira o 1º número: "))
num2 = float(input("Insira o 2º número: "))

if operador == "+":
    resultado = num1 + num2
    print(round(resultado, 3))

elif operador == "-":
    resultado = num1 - num2
    print(round(resultado, 3))

elif operador == "*":
    resultado = num1 * num2
    print(round(resultado, 3))

elif operador == "/":
    resultado = num1 / num2
    print(round(resultado, 3))

else:
    print(f"{operador} não é valido")
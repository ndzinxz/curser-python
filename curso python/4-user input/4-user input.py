

name = input("Qual seu nome?: ")
age = int(input("Qual a sua idade?: ")) 
location = input("Onde você mora? :")

#pode usar | age = int(input("...")) |
#          | age = int(age) |

age = age * 1

print(f"Olá {name}!")
print("Feliz aniversário")
print(f"Sua idade é {age}")
print(f"Você mora na cidade de(o) {location}")
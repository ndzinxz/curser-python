num = 5
a = 6
b = 7
idade = 14
temperatura = 19
função_usuario = "adm"
#print("Positivo" if num > 0 else "Negativo")
#resultado = "impar" if num % 2 == 0 else "par"
#max_num = a if a > b else b
#min_num = a if a < b else b
#status = "Adulto" if idade >= 18 else "Criança"
#clima = "QUENTE" if temperatura > 20 else "FRIO"
nivel_acesso = "Acesso Total" if função_usuario == "adm" else "Acesso limitado"

print(nivel_acesso)
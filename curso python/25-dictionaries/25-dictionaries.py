capitais = {"Brasil": "Brasilia",
            "India": "New Delhi",
            "China": "Beijing",
            "Argentina": "Buenos Aires"}

# print(dir(capitais))
# print(help(capitais))
# print(capitais.get("Brasil"))

# if capitais.get("Brasil"):
#     print("Essa capital existe")
# else:
#     print("Essa capital nao existe")

# capitais.update({"Portugal": "Lisboa"})
# capitais.pop("India")
# capitais.popitem()
# capitais.clear()

# chaves = capitais.chaves()
# for chave in capitais.chaves():
# print(key)

# itens = capitais.items()
for chave, valor in capitais.items():
    print(f"{chave}: {valor}")

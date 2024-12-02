mantimentos = {
    "frutas": {"banana", "laranja", "manga", "uva"},
    "vegetais": {"alface", "cenoura", "brócolis", "espinafre"},
    "carnes": {"frango", "picanha", "costela", "alcatra"},
}

for collection in mantimentos.values():
    for comida in collection:
        print(comida, end=" ")
    print()

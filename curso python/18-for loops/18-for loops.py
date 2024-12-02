for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

print("-----------------------------")

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

print("-----------------------------")

for x in (1, 11):
    print(x)

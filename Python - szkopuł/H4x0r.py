odp = input()
t = []

for i in range(0, len(odp)):
    if odp[i] == "a":
        t.append("4")
    elif odp[i] == "e":
        t.append("3")
    elif odp[i] == "i":
        t.append("1")
    elif odp[i] == "o":
        t.append("0")
    elif odp[i] == "s":
        t.append("5")
    else:
        t.append(odp[i])

joined = "".join(t)
print(joined)

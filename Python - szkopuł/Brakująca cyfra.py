odp = input()
t = []
t2 = []
x = 1
suma = 0

for i in range(0, len(odp)):
    if ord(odp[i]) >= 48 and ord(odp[i]) <= 57:
        t.append(odp[i])
    elif ord(odp[i]) == 88:
        t2.append(odp[i])

for i in range(0, len(t)):
    t[i] = int(t[i])

for i in range(0, len(t)):
    suma += t[i]

for i in range(9):
    if (suma + x) % 9 == 0:
        print(x)
        break
    else:
        x += 1


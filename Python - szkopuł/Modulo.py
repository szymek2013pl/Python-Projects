t = []
t1 = []

for i in range(15):
    n = int(input())
    reszta = n % 37
    t.append(reszta)

for i in range(len(t)):
    for j in range(0, len(t) - 1):
        if t[j] < t[j + 1]:
            x = t[j + 1]
            t[j + 1] = t[j]
            t[j] = x

for z in range(0, len(t) - 1):
    if t[z] != t[z + 1]:
        t1.append(t[z])


for i in range(len(t)):
    for j in range(0, len(t) - 1):
        if t[j] < t[j + 1]:
            x = t[j + 1]
            t[j + 1] = t[j]
            t[j] = x

t1.append(t[0])

print(len(t1))

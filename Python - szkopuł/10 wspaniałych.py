n = int(input())
t = []
t2 = []

for i in range(n):
    odp = int(input())
    t.append(odp)

for i in range(len(t)):
    for a in range(len(t) - 1):
        if t[a + 1] > t[a]:
            x = t[a]
            t[a] = t[a + 1]
            t[a + 1] = x

print(t)
if len(t) > 10:
    for i in range(0, 10):
        t2.append(t[i])
    print(t2)

else:
    print(t)



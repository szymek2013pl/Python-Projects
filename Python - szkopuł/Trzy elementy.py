n = int(input("Rozmiar: "))
t = []
k = 0
a = 0

for i in range(n):
    odp = int(input())
    t.append(odp)

for y in range(0, n - 1):
    for x in range(0, len(t) - 1):
        if t[x] == t[a]:
            k += 1
            if t[x] == t[len(t) - 1] and k < 3:
                k = 0
    a += 1

if k >= 3:
    print("TAK")
else:
    print("NIE")

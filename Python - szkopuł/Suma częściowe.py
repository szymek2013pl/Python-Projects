n = int(input())
a = []
b = []
suma = 0
y = 1

for i in range(n):
    odp = int(input())
    a.append(odp)

x = len(a) - 1

while x >= 0:
    suma += a[x]
    b.append(suma)
    x -= 1

for i in range(len(b) - 1):
    for a in range(0, len(b) - y):
        if b[a] < b[a + 1]:
            m = b[a + 1]
            b[a + 1] = b[a]
            b[a] = m
    y += 1

print(b)

    

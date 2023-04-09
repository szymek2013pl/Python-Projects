z = int(input())
t = []
c = 1

for i in range(z):
    odp = input()
    t.append(odp)

t.sort()

for b in range(len(t)):
    for a in range(0, len(t) - c):
        if len(t[a]) > len(t[a + 1]):
            x = t[a + 1]
            t[a + 1] = t[a]
            t[a] = x
    c += 1

a = 0
while a < len(t):
    print(t[a])
    a += 1
    

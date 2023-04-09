z = int(input())
t = []
y = 1
c = 1
if z <= 150:
    for i in range(z):
        odp = input()
        t.append(odp)
    for i in range(len(t) - 1):
        for a in range(0, len(t) - y):
            if t[a] > t[a + 1]:
               x = t[a + 1]
               t[a + 1] = t[a]
               t[a] = x
        y += 1

    if len(t[a]) < 200:
        for b in range(len(t)):
            for a in range(0, len(t) - c):
                if len(t[a]) < 200:
                    if len(t[a]) > len(t[a + 1]):
                        x = t[a + 1]
                        t[a + 1] = t[a]
                        t[a] = x
            c += 1
        a = 0
        while a < len(t):
            print(t[a])
            a += 1
    else:
        print("Musisz podać krótszy wyraz")
        
else:
    print("Musisz podać mniejszą liczbę")

tekst1 = input()
tekst2 = input()
t1 = []
t2 = []

for i in range(0, len(tekst1)):
    t1.append(tekst1[i])

for i in range(0, len(tekst2)):
    t2.append(tekst2[i])

t1.sort()
t2.sort()

if t1 == t2:
    print("TAK")
else:
    print("NIE")

    

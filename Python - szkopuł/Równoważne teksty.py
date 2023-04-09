tekst1 = input()
tekst2 = input()
t1 = []
t11 = []
t2 = []
t22 = []

for i in range(0, len(tekst1)):
    if i < len(tekst1) // 2:
        t1.append(tekst1[i])
    else:
        t11.append(tekst1[i])

for i in range(0, len(tekst2)):
    if i < len(tekst2) // 2:
        t2.append(tekst2[i])
    else:
        t22.append(tekst2[i])

t1.sort()
t11.sort()
t2.sort()
t22.sort()

if t1 == t2 or t1 == t22 or t11 == t2 or t11 == t22:
    print("TAK")
else:
    print("NIE")



    

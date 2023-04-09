odp = int(input())
t = []

for i in range(1, odp + 1):
    if odp % i == 0:
        t.append(i)
        if len(t) == 3:
            break
    else:
        continue

if len(t) > 2 or odp == 0 or odp == 1:
    print("NIE")
else:
    print("TAK")

    

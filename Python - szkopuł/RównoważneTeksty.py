a = input()
b = input()

t_a1 = []
t_a2 = []
t_b1 = []
t_b2 = []

for i in range(0, len(a)):
    if i < len(a) // 2:
        t_a1.append(a[i])
    elif i >= len(a) // 2:
        t_a2.append(a[i])

for i in range(0, len(b)):
    if i < len(b) // 2:
        t_b1.append(b[i])
    elif i >= len(b) // 2:
        t_b2.append(b[i])

t_a1.sort()
t_a2.sort()
t_b1.sort()
t_b2.sort()

if (a == b) or (t_a1 == t_b1 and t_a2 == t_b2 or t_a1 == t_b2 and t_a2 == t_b1):
    print("TAK")
else:
    print("NIE")

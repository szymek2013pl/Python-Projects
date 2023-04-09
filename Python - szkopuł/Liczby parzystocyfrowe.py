n = int(input())
n1 = n
t = []
t1 = []

while n >= 0:
    reszta = n1 % 5
    n1 = n1 // 5
    t.append(2 * reszta)
    n -= 1
    if n1 == 0:
        break

a = len(t) - 1
while a >= 0:
    t1.append(str(t[a]))
    a -= 1

joined = "".join(t1)
print(joined)
 

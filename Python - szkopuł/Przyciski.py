n, m = input().split()
n = int(n)
m = int(m)
t = []
t_odp = list(map(int, input().split()))
x = 0
naj = 0

for i in range(n):
    t.append(0)

for i in range(m):
    x = t_odp[i]
    t[x - 1] += 1
    if x == n + 1:
        for i in range(n):
            if t[i] > naj:
                naj = t[i]
            t[i] = naj

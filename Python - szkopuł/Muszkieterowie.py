n = int(input())
t = []
index = 0

t = list(map(int, input().split()))
t.sort()

if len(t) > 10:
    while t[n - 1] < t[9]:
        del t[n - 1]
        n -= 1
        
while index <= 9:
    print(t[index], end=" ")
    index += 1

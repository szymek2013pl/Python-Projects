n = int(input())
t = list(map(int, input().split()))

t.sort()
index = len(t) - 1

if n >= 10:
    while index >= n - 10:
        print(t[index], end=" ")
        index -= 1
else:
     while index >= 0:
        print(t[index], end=" ")
        index -= 1
    

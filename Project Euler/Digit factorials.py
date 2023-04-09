def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

arr = []
aggregate = 0
temp_aggregate = 0

for i in range(3, 1000):
    num = i
    num = str(num)
    for j in range(0, len(num)):
        arr.append(int(num[j]))
        temp_aggregate += factorial(num[j])
        if temp_aggregate == i:
            aggregate += i

print(aggregate)
        

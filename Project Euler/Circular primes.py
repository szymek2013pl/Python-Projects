import math

def is_prime(n):
    if n == 0 or n == 1:
        return 0
    for i in range(2, sqrt(n)):
        if (n % i == 0):
            return 0
    return 1

def circle(m):
    for i in range(len(m) - 1):
        for j in range(0, len(m)):
            x = m[j]
            m[j + 1] = m[j]

amount = 0
arr = []

for i in range(0, 1_000_000):
    if is_prime(i) == 1:
        num = i
        num = str(num)
        for j in range(0, len(num)):
            arr.append(num[j])

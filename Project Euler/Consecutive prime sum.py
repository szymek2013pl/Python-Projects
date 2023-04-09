def is_prime(n):
    if n == 0 or n == 1:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1

def make_prime(n):
    num = 0
    total = 0
    while total <= n:
        if is_prime(num) == 1:
            total += num
        num += 1
    if total == n:
        return 1
    return 0

num = 1_000_000

while num >= 953:
    if make_prime(num) == 1 and is_prime(num) == 1:
        print(num)
    else:
        num -= 1


def binary(n):
    arr = []
    while n != 0:
        arr.append(n % 2)
        n = n // 2
    arr.reverse()
    num = ""
    for i in range(0, len(arr)):
        num += str(arr[i])
    return num

def is_palindrome(m):
    m = str(m)
    if m == m[::-1]:
        return 1
    return 0

num = 1
amount = 0

while num < 1_000_000:
    if is_palindrome(num) == 1:
        num2 = binary(num)
        if is_palindrome(num2) == 1:
            amount += num
    num += 1

print(amount)



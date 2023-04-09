arr = [1, 1]
index = 2
total = 0
fib = 0

while fib < 4000000:
    fib = arr[index - 1] + arr[index - 2]
    arr[index - 2] = arr[index - 1]
    arr[index - 1] = fib
    if fib % 2 == 0:
        total += fib
    index += 1

print(fib)



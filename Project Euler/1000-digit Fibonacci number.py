fib1 = 1
fib2 = 1
odp = 0
index = 2

while True:
    odp = fib1 + fib2
    fib2 = fib1
    fib1 = odp
    index += 1
    odp = str(odp)
    if len(odp) == 1000:
        break

print(index)

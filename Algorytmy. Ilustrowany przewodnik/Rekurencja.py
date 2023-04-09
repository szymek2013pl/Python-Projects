# - odliczanie
def countdown(i):
    print(i)
    if i <= 0:
        return
    else:
        countdown(i - 1)

countdown(15)

# - silnia
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

m = 5
print(factorial(m))

# - ciag fibonacciego
def fib(n):
    if n < 3:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

m = 10
print(fib(m))

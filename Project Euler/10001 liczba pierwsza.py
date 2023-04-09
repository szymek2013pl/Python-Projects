import math
n = int(input("Podaj n: "))

if n % math.sqrt(n) != 0:
    print("Tak")
elif n == 1 or n == 0:
    print("Nie")
else:
    print("Nie")

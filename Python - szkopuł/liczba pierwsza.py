n = int(input())
a = 2
licznik = 0
for i in range(2, n//2):
    while a <= n/2:
        if n % i == 0:
            licznik = 1
        else:
            licznik = 0
        a += 1

if licznik >= 1:
    print("Nie")
else:
    print("Tak")
            

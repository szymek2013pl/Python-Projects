n = int(input())
T = []

for i in range(2, n * 100):
    T.append(i)

dzielnik = 2

for i in range(2, n):
    indeks = 0
    while indeks <= n * 5:
        if (T[indeks] != dzielnik and T[indeks] % dzielnik == 0):
            del T[indeks]
        indeks += 1
    dzielnik += 1

for i in range(0, n):
    print(T[i])
    



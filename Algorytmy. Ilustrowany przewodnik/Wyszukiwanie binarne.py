n = int(input('Podaj liczbe elementow: '))

arr = []

for i in range(0, n):
    odp = int(input('Podaj element: '))
    arr.append(odp)

item = int(input('Pozycji jakiego elementu szukasz: '))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    guess = arr[mid]
    if guess == item:
        print(str(item) + ' na pozycji ' + str(mid))
    if guess > item:
        high = mid - 1
    else:
        low = mid + 1


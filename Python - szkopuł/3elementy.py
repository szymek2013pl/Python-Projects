n = int(input())
lista = list(map(int, input().split()))
ile = 0
x = 0

lista.sort()

for i in range(n):
    for j in range(0, len(lista)):
        if lista[i] == lista[j]:
            ile += 1
            if ile == 3:
                x = ile
        else:
            ile = 0
            
ile = x

if ile >= 3:
    print("TAK")
else:
    print("NIE")


    

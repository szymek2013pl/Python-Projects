a, b = input().split()
a = int(a)
b = int(b)

def NWW(a, b):
    b1 = b
    if a % b1 == 0:
        c = a // b
    while a % b1 != 0 or b % b1 != 0:
        b1 -= 1
        if a % b1 == 0 and b % b1 == 0:
            print(a * b // b1)
NWW(a, b)



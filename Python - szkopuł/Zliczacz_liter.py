n = int(input())
ile = 0
t = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z", "A", "B", "B", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z"]
litery = []
liczniki = []

for i in range(n):
    odp = input()
    for j in range(len(t)):
        for k in range(len(odp)):
            if t[j] == odp[k]:
                ile += 1
            
    



 

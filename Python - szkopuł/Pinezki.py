n = int(input())
t = []
ile = 0
x = 0

for i in range(n):
    odp = int(input())
    t.append(odp)

for i in range(0, n):
    if t[i] == 1:
        ile += 1
    elif t[i] == 0:
        if x >= ile:
            ile = 0
        else:
            x = ile
            ile = 0

if ile >= x:
    print(ile)
else:
    print(x)

        

        
        
        
    
        
        
        

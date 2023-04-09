n = int(input())
o_ile = int(input())
t1 = []
t3 = []
a = 0

for i in range(n):
    odp = input()
    t1.append(odp)

for i in range(n):    
    joined = ""
    t2 = []
    for j in range(0, len(t1[i])):
        t2.append(t1[i][j])
        if ord(t2[j]) >= 65 and ord(t2[j]) <= 90: 
            t2[j] = ord(t2[j])
            if t2[j] + o_ile <= 90: 
                t2[j] += o_ile
            else:
                t2[j] = 65 + ((t2[j] + o_ile) - 91)
            t2[j] = chr(t2[j])
        else:
            break   
        joined = "".join(t2)
    t3.append(joined)

while a < n:
    print(t3[a])
    a += 1
        
        






    
    
    

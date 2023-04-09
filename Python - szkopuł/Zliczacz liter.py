n = int(input())
ile = 0
t = [] #caly wyraz
t1 = [] #wielkie litery
t2 = [] #do porownania
t3 = []

for i in range(n):
    odp = input()
    for i in range(0, len(odp)):
        if odp[i] != " " and ord(odp[i]) > 96:
            t.append(odp[i])
        elif ord(odp[i]) > 64 or ord(odp[i]) < 91 and odp[i] != " ":
            t1.append(odp[i])

t.sort()
t1.sort()

for i in range(0, len(t1)):
    t.append(t1[i])

for i in range(0, len(t)):
    if t[i] != t[i - 1]:
        t2.append(t[i])

for i in range(0, len(t)):
    for j in range(0, len(t2)):
        if t[i] == t2[j]:
            ile +=1
        if t2[j] == t2[len(t2) - 1]:
            t3.append(ile)
            ile = 0

print(t3)
for i in range(0, len(t2)):
    print(t2[i], t3[i])

        
            
            




        




        
    
        

        





   
        
        




            

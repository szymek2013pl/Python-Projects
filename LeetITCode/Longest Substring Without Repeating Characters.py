'''
s = "abcabcbb"
my_dict = {}
amount = 0

for i in range(0, len(s)):
    my_dict[s[i]] = -1
        
for i in range(0, len(s)):
    if my_dict[s[i]] == -1:
        my_dict[s[i]] = i

print(my_dict["c"])
'''

l1 = [2, 4, 3]
l1.reverse()
num1 = ''
for i in range(0, len(l1)):
    num1 += str(l1[i])
num1 = int(num1)
        
l2 = [5, 6, 4]
l2.reverse()
num2 = ''
for i in range(0, len(l2)):
    num2 += str(l2[i])
num2 = int(num2)
        
num3 = num1 + num2
arr = []
        
while num3 != 1:
    num3 = num3 // 10
    arr.append(num3 % 10)
arr.reverse()
print(arr)


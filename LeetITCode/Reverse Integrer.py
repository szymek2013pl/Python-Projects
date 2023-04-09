'''
x = int(input())
x = str(x)
x = x[::-1]
x = int(x)
print(x)
'''

nums = [3, 2, 4]
target = 6
arr = []
for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            arr.append(i)
            arr.append(j)
print(arr)

def check(a):
    div = []
    for i in range(1, a):
        if a % i == 0:
            div.append(i)
    sum1 = sum(div)
    return sum1

num = 0
amount = 0

while num < 10000:
    num2 = check(num)
    if check(num2) == num and num != num2:
        amount += num
    num += 1

print(amount)





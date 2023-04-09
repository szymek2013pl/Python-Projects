num = 1
amount = 0

for i in range(1, 101):
    num *= i

while num != 0:
    amount += num % 10
    num = num // 10

print(amount)

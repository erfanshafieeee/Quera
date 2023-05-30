n = int(input())
sum = 0
count = 0

for i in range(1, n + 1):
    for j in range(1, ((i + 1)//2 + 2)):
        if i % j == 0:
            sum += j
            count += 1
    if i > 3:
        sum += i
        count += 1
print(count, sum)
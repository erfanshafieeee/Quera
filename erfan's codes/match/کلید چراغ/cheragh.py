n = int(input())
i = 0
counter = 0
x2 = int(input())
while i < n-1:
    x1 = int(input())
    if x1 != x2:
        counter = counter+1

    i = i+1
    x2 = x1
print(counter)

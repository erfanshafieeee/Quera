lower = int(input())
upper = int(input())
list_num = []

for num in range(lower+1, upper):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            list_num.append(num)

for g in list_num:
    if g != list_num[-1]:
        print(g, end=",")
    else:
        print(g)

string = input()
n, m = sorted([int(i) for i in string.split(" ")])

n1, m1 = n, m
while m:
    n, m = m, n % m
print(n, m1 * n1 // n)

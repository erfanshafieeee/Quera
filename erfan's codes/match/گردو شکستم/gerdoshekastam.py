n, x, y = map(int, input().split())
b = 0
while b*y <= n:
    if (n-b*y) % x == 0:
        print((n-b*y)//x, b)
        break
    b += 1
else:
    print(-1)

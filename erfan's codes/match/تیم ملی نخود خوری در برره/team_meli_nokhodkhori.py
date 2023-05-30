a, b, c = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
arr = []
for x in (x1, x2, x3):
    arr.append((x, False))
for y in (y1, y2, y3):
    arr.append((y, True))

arr.sort()

s = 0
t = -1
for i in range(len(arr) - 1):
    if arr[i][1] == False:
        t += 1
    else:
        t -= 1
    s += [a, b, c][t] * (arr[i + 1][0] - arr[i][0]) * (t + 1)

print(s)
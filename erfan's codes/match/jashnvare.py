x = int(input())
v = []
m = []
for num in range(2, x+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            m.append(num)

for i in range(2, x+1):
    if x % i == 0:
        v.append(i)

p = len(m)
w = m[p-1]
if x == w:
    print(1)
else:
    v.remove(x)
    print(v[-1])

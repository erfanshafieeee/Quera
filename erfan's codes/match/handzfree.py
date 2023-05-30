l1, r1 = input().split()
l2, r2 = input().split()
if l1 == r1 or l2 == r2:
    print("YES")
else:
    if l1 == r2 or r1 == l2:
        print("YES")
    else:
        print("NO")
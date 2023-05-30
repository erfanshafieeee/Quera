a, b = map(int, input().split())
if a == 0 and b != 0:
    print("invalid")
if a == 0 and b == 0:
    print("infinite")
if a != 0 and b != 0 - b/a != 0:
    print("unique")
if a!=0 and b==0:
    print("unique")
n, m = input().split()
m = int(m)
n = int(n)
for number in range(n):
    print(f"{'X'*m}{'.'*m}{'X'*m}")
for number in range(n):
    print(f"{'.'*m}{'X'*m}{'.'*m}")
for number in range(n):
    print(f"{'X'*m}{'.'*m}{'X'*m}")
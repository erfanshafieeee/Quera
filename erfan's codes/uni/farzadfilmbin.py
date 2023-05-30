n = int(input())
lister = []
for i in range(n):
    j = input()
    lister.append(j.title())
print("\n".join(lister))
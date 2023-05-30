n, k = [int(i) for i in input().split()]

turn = 1
count = 1
while True:
    turn += k
    turn = (turn - n) if turn > n else turn

    if turn == 1:
        break
    count += 1

print(count)
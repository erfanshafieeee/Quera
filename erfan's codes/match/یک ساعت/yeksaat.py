hour, min = [int(i) for i in input().split()]
min = "00" if min == 0 else str(60 - min)
hour = "00" if hour == 0 else str(12 - hour)

if len(min) < 2:
    min = "0" + min

if len(hour) < 2:
    hour = "0" + hour

print(f'{hour}:{min}')
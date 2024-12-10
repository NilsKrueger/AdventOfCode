import pandas as pd

f = open('input.txt', 'r')
sum = 0

for l in f:
    list = [int(x) for x in l.split()]
    print(list)

    current = list[0]
    asc = list == sorted(list)
    dec = list == sorted(list, reverse = True)

    safe = True

    for i in range(0, len(list)-1):
        next = list[i + 1]

        # ascending
        if asc:
            if next - current < 1 or next - current > 3:
                safe = False
        # decending
        elif dec:
            if current - next < 1 or current - next > 3:
                safe = False
        else:
            safe = False

        current = next

    if safe:
        sum += 1

print(sum)
f.close()
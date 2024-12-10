import pandas as pd

f = open('input.txt', 'r')
sum = 0
sum_good = 0

def is_safe(list):
    asc = list == sorted(list)
    dec = list == sorted(list, reverse = True)

    safe = True
    for i in range(0, len(list)-1):
        dist = abs(list[i] - list[i+1])

        if (dist < 1 or dist > 3):
            safe = False
    return safe and (asc or dec)

for l in f:
    list = [int(x) for x in l.split()]
    print(list, end = "")

    current = list[0]
    safe = is_safe(list)

    print(' safe', safe, end = "")
    if safe:
        sum += 1

    good = False
    for i in range(len(list)):
        l2 = list[:i] + list[i+1:]
        if is_safe(l2):
            good = True
    if good:
        sum_good += 1
    print(' good', good)

print('Safe ', sum)
print('Good ', sum_good)
f.close()
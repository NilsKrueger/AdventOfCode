import re
import math

f = open('input.txt', 'r')

sum = 0

lines = " ".join(line.strip() for line in f)

dos = lines.split("do()")
for item in dos:
    clean_item = re.sub(r"don't[(][)].*", '', item)
    muls = re.findall('mul[(]{1}[0-9]{1,3},[0-9]{1,3}[)]{1}', clean_item)

    for s in muls:
        mul = list(map(int, s.strip('mul()').split(',')))
        sum += math.prod(mul)

print('Sum: ', sum)
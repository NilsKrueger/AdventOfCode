import re
import math

f = open('input.txt', 'r')

sum = 0

for l in f:
    lines = re.findall('mul[(]{1}[0-9]{1,3},[0-9]{1,3}[)]{1}', l)

    for s in lines:
        mul = list(map(int, s.strip('mul()').split(',')))
        sum += math.prod(mul)

print('Sum: ', sum)
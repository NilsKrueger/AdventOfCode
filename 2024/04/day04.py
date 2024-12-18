
f = open('input.txt', 'r')

sum = 0
data = []

for line in f:
    data.append(list(line.strip('\n')))

l = len(data)
print('Length data: ', l)

def hasX(line, col):
    return (((data[line][col] == 'M' and data[line+1][col+1] == 'A' and data[line+2][col+2] == 'S') or
             (data[line][col] == 'S' and data[line+1][col+1] == 'A' and data[line+2][col+2] == 'M')) 
             and
            ((data[line][col+2] == 'M' and data[line+1][col+1] == 'A' and data[line+2][col] == 'S') or
             (data[line][col+2] == 'S' and data[line+1][col+1] == 'A' and data[line+2][col] == 'M')))

for line in range(l):
    r = len(data[line])
    print('------line:', line)

    for col in range(r):
        print('| col:', col)
        if line <= l - 3 and col <= r - 3:
            if hasX(line, col): 
                print('hit in line', line, 'and column', col)
                sum += 1
print(sum)

f = open('input.txt', 'r')

sum = 0
data = []

for line in f:
    data.append(list(line.strip('\n')))

l = len(data)
print('Length data: ', l)

def hor(line, col):
    valid = ((data[line][col] == 'X' and data[line][col+1] == 'M' and data[line][col+2] == 'A' and data[line][col+3] == 'S') or
             (data[line][col] == 'S' and data[line][col+1] == 'A' and data[line][col+2] == 'M' and data[line][col+3] == 'X'))
    if valid: print('hor: ', data[line][col], data[line][col+1], data[line][col+2], data[line][col+3])

    return valid

def ver(line, col):
    valid = ((data[line][col] == 'X' and data[line+1][col] == 'M' and data[line+2][col] == 'A' and data[line+3][col] == 'S') or
             (data[line][col] == 'S' and data[line+1][col] == 'A' and data[line+2][col] == 'M' and data[line+3][col] == 'X'))
    if valid: print('ver: ', data[line][col], data[line+1][col], data[line+2][col], data[line+3][col])

    return valid

def diaR(line, col):
    valid = ((data[line][col] == 'X' and data[line+1][col+1] == 'M' and data[line+2][col+2] == 'A' and data[line+3][col+3] == 'S') or
             (data[line][col] == 'S' and data[line+1][col+1] == 'A' and data[line+2][col+2] == 'M' and data[line+3][col+3] == 'X'))
    if valid: print('diaR:', data[line][col], data[line+1][col+1], data[line+2][col+2], data[line+3][col+3])

    return valid

def diaL(line, col):
    valid = ((data[line][col] == 'X' and data[line+1][col-1] == 'M' and data[line+2][col-2] == 'A' and data[line+3][col-3] == 'S') or
             (data[line][col] == 'S' and data[line+1][col-1] == 'A' and data[line+2][col-2] == 'M' and data[line+3][col-3] == 'X'))
    if valid: print('diaL:', data[line][col], data[line+1][col-1], data[line+2][col-2], data[line+3][col-3])

    return valid

for line in range(l):
    r = len(data[line])
    print('------line:', line)

    for col in range(r):
        print('| col:', col)
        if col < l - 3:
            if hor(line, col): sum += 1
        if line < r - 3:
            if ver(line, col): sum += 1
        if col < l - 3 and line < r - 3:
            if diaR(line, col): sum += 1
        if col >= 3 and line < l - 3:
            if diaL(line, col): sum += 1
print(sum)
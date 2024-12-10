import pandas as pd

data_df = pd.read_csv('input.csv', sep = " ", header = None)

# sort the columns, index have to be reseted since it is part of the sort
left = data_df[0].sort_values().reset_index(drop=True)
right = data_df[1].sort_values().reset_index(drop=True)
sum = 0
sim = 0

# combine to new df with individual sorted values
merged = pd.DataFrame({'left': left, 'right': right})

# iterate over rows and create sum of all rows
for row in merged.itertuples():
    #print(row[1], row[2], abs(row[1] - row[2]))
    sum = sum + abs(row[1] - row[2])

    value = row[1]
    count = len(merged[merged['right'] == value])
    sim = sim + (value * count)

print('Part 1: ', sum)
print('Part 2: ', sim)
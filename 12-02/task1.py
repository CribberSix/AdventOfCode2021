import csv

with open("c:/coding/repositories/AdventOfCode2021/2021-12-02/data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    data = [(x[0], int(x[1])) for x in list(reader)]

depth = 0
horizontal = 0

for movement, count in data:
    if movement == 'forward':
        horizontal += count
    elif movement == 'down':
        depth += count
    elif movement == 'up':
        depth -= count

print(depth, horizontal)
print(depth * horizontal)

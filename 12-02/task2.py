import csv

with open("data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    data = [(x[0], int(x[1])) for x in list(reader)]

depth = 0
horizontal = 0
aim = 0

for movement, count in data:
    if movement == 'forward':
        horizontal += count
        depth += (aim * count)
    elif movement == 'down':
        aim += count
    elif movement == 'up':
        aim -= count

print(depth, horizontal)
print(depth * horizontal)

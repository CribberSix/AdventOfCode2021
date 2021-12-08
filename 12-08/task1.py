# Parse data
with open("data.txt") as f:
    data = [x[:-1].split(' | ') for x in f.readlines()]
    data = [[row[0].split(' '), row[1].split(' ')] for row in data]

counter = 0
for row in data:
    for element in row[1]:
        if len(element) in [2, 3, 4, 7]:
            counter += 1
print(counter)

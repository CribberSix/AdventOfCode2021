
# Surround data with 9s so we don't have to take special care of edges while identifying low points
# Since it's a 9, even low points on the actual edges remain low points.
with open("data.txt") as f:
    data = [[9] + [int(e) for e in row] + [9] for row in [list(x[:-1]) for x in f.readlines()]]
    data = [[9] * (len(data[0]) + 2)] + data
    data = data + [[9] * (len(data[0]) + 2)]

# identify low points
low_points = []
for y, row in enumerate(data):
    for x, element in enumerate(row):
        try:
            if data[y][x+1] > element and data[y][x-1] > element and data[y+1][x] > element and data[y-1][x] > element:
                low_points.append(element)
        except IndexError:  # edges are artifically added, so we can disregard them.
            pass

print(f"Solution: {sum(low_points) + len(low_points)}.")

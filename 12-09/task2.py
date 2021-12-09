from typing import List
# Surround data with 9s so we don't have to take special care of edges while identifying low points
# Since it's a 9, even low points on the actual edges remain low points.
with open("data.txt") as f:
    data = [[9] + [int(e) for e in row] + [9] for row in [list(x[:-1]) for x in f.readlines()]]
    data = [[9] * (len(data[0]) + 2)] + data
    data = data + [[9] * (len(data[0]) + 2)]


def get_low_points(data: List) -> List:
    """Get lowest points in the field."""
    low_points = []
    for y, row in enumerate(data):
        for x, element in enumerate(row):
            try:
                if data[y][x+1] > element and data[y][x-1] > element and data[y+1][x] > element and data[y-1][x] > element:
                    low_points.append((y, x, element))
            except IndexError:  # edges are artifically added, so we can disregard them.
                pass
    return low_points


def is_valid_index(x: int, y: int, data: List) -> bool:
    """Check if the index we want to access is valid."""
    try:
        x = data[x][y]
        return True
    except IndexError:
        return False


def get_list_of_neighbours(y: int, x: int, element: int) -> List:
    """Recursively add all neighbours that flow into the current one."""
    global data
    res = [(y, x, element)]
    if is_valid_index(y, x + 1, data) and element < data[y][x + 1] < 9:
        res += get_list_of_neighbours(y, x+1, data[y][x+1])
    if is_valid_index(y, x - 1, data) and element < data[y][x - 1] < 9:
        res += get_list_of_neighbours(y, x-1, data[y][x-1])
    if is_valid_index(y + 1, x, data) and element < data[y + 1][x] < 9:
        res += get_list_of_neighbours(y+1, x, data[y+1][x])
    if is_valid_index(y - 1, x, data) and element < data[y - 1][x] < 9:
        res += get_list_of_neighbours(y-1, x, data[y-1][x])
    return res


basin_sizes = []
basins = []
for point in get_low_points(data):
    neighbours = get_list_of_neighbours(point[0], point[1], point[2])
    # remove duplicates as a neighbour can be the lowest neighbour of multiples.
    basins.append(set(neighbours))
    basin_sizes.append(len(set(neighbours)))

basin_sizes.sort()
print(f"Solution: {(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])}")

# from visualize_basins import visualize_basins
# visualize_basins(basins, len(data), len(data[0]))

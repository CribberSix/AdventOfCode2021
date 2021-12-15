import math, sys


def get_neighbour_inidizes(node):
    global grid
    _neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    return [(node[0]+ny, node[1]+nx) for nx, ny in _neighbours if 0 <= node[0]+ny < len(grid) and 0 <= node[1]+nx < len(grid[0])]


with open("data.txt") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

# Create a new "super grid":
super_grid = []
lg = len(grid)

for cy in range(0, 5 * lg):
    super_grid.append([])  # add a new empty row
    for cx in range(0, 5 * lg):

        if 0 <= cy < lg and 0 <= cx < lg:  # if we are in first tile, just copy the original value.
            super_grid[cy].append(grid[cy][cx])

        elif cy >= lg and cx < lg:  # first tile column -> copy value from the top (one length upwards)
            new_value = super_grid[cy-lg][cx] + 1
            if new_value > 9:
                new_value = 1
            super_grid[cy].append(new_value)

        elif cx >= lg:  # all other tile columns -> copy value from the left (one width to the left)
            new_value = super_grid[cy][cx - lg] + 1
            if new_value > 9:
                new_value = 1
            super_grid[cy].append(new_value)

grid = super_grid  # overwrite grid.

# dict of all nodes and their respective costs to reach them
distances = {(i, j): math.inf for i in range(len(grid[0])) for j in range(len(grid))}
prio_queue = {(0, 0): 0}  # dict of all nodes which are reachable and whose cost got updated.

# Start in the top left:
distances[(0, 0)] = 0  # starting node has no cost to itself.

while len(prio_queue) > 0:

    # Select the cheapest node from the queue for the next iteration
    current_node = min(prio_queue, key=prio_queue.get)
    current_node_cost = prio_queue[current_node]
    del prio_queue[current_node]  # remove node from priority queue

    # check for last node
    if current_node == (len(grid)-1, len(grid)-1):
        print("Last node: ", current_node_cost)
        break

    # assemble all neighbours of the current node
    neighbours = get_neighbour_inidizes(current_node)
    ns = {(iy, ix): grid[iy][ix] for iy, ix in neighbours}

    # For all neighbours:
    # 1. Calculate the cost to reach the neighbour from the current node.
    # 2. IF the cost of the path from the current node is cheaper than another path from before,
    #   update the cost to reach the node
    #   add it to the prio queue again (revisit if necessary - possible since we don't have negative values)
    for n in ns:
        cost_to_reach_n = distances[current_node] + grid[n[0]][n[1]]
        if cost_to_reach_n < distances[n]:
            distances[n] = cost_to_reach_n
            prio_queue[n] = cost_to_reach_n

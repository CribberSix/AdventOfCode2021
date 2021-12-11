from typing import List, Tuple


def get_neighbours(y: int, x: int, cl: int, rl: int) -> List[Tuple[int, int]]:
    """Get neighbouring indizes within the matrix.
    :param y: y-index of current octopus
    :param x: x-index of current octopus
    :param cl: column length of the matrix
    :param rl: row length of the matrix
    """
    neighbours = [
                  (y+i, x+j)
                  for i in range(-1, 2)
                  for j in range(-1, 2)
                  if (i, j) != (0, 0) and 0 <= y+i < cl and 0 <= x+j < rl
                  ]
    return neighbours


def increment_octopi(y: int, x:int) -> None:
    """
    Increments the current octopus by one.
    If its level reaches 10, then we call upon its neighbours to be incremented as well.
    """
    global octopi, flashes_counter
    octopi[y][x] += 1
    if octopi[y][x] == 10:  # only flash on first increment greater than 9
        flashes_counter += 1
        neighbours = get_neighbours(y, x, len(octopi), len(octopi[0]))
        for (ny, nx) in neighbours:
            increment_octopi(ny, nx)


# Parse data
with open("data.txt") as f:
    octopi = [[int(e) for e in x[:-1]] for x in f.readlines()]

# Rounds:
flashes_counter = 0
for i in range(100):
    # increment all octopi by one and if flashing, increment neighbours.
    for y, row in enumerate(octopi):
        for x, octopus in enumerate(row):
            increment_octopi(y, x)

    # reset energy levels of all octopi who have an energy level above 9
    octopi = [[o if o <= 9 else 0 for o in row] for row in octopi]

    print(f"ROUND {i+1} with {flashes_counter} flashes since the start.")

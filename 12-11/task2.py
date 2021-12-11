from typing import List
from task1 import increment_octopi


def check_all_flashing(octopi: List) -> bool:
    for row in octopi:
        for octopus in row:
            if octopus <= 9:
                return False
    return True


# Parse data
with open("data.txt") as f:
    octopi = [[int(e) for e in x[:-1]] for x in f.readlines()]

# Rounds:
flashes_counter = 0
i = -1
while True:
    i += 1  # round counter

    # increment all octopi by one and if flashing, increment neighbours.
    for y, row in enumerate(octopi):
        for x, octopus in enumerate(row):
            increment_octopi(y, x)

    print(f"ROUND {i+1} with {flashes_counter} flashes since the start.")

    if False:  # visualize octopi
        for s in [[str(o) for o in row] for row in octopi]:
            print("".join(s))

    if check_all_flashing(octopi):
        print("ALL FLASHING.")
        break

    # reset energy levels of all octopi who have an energy level above 9
    octopi = [[o if o <= 9 else 0 for o in row] for row in octopi]

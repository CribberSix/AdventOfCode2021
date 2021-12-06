from copy import deepcopy


with open("data.txt") as f:
    fishes = [int(x) for x in f.read().split(",")]

fishes_new = []
for day in range(256):
    print(day)
    for fish in fishes:

        if fish == 0:
            fishes_new.append(6)  # reset fish
            fishes_new.append(8)  # spawn new fish
        else:
            fishes_new.append(fish-1)  # subtract counter from fish

    fishes = deepcopy(fishes_new)
    fishes_new = []

print(len(fishes))

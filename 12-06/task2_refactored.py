# parse data
with open("data.txt") as f:
    data = [int(x) for x in f.read().split(",")]

# Using a dict to store the number of fishes which are in a certain day of the cycle.
fishes = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
for f in data:
    fishes[f] += 1

# Iterate over days
for day in range(18):
    fishes = {n: fishes[n+1] for n in range(-1, 8)}  # nested loop for dicts!
    fishes[8] = fishes[-1]
    fishes[6] += fishes[-1]
    fishes[-1] = 0

count_fishes = sum([fishes[key] for key in fishes])
print(count_fishes)

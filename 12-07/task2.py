# Parse data
with open('data.txt') as f:
    data = [int(x) for x in f.readlines()[0].split(',')]

# calculate fuel costs of moving all elements to the current index position.
options = []
for index in range(0, max(data)+1):
    fuel_cost = 0
    for position in data:
        diff = abs(index-position)
        fuel_cost += ((diff ** 2) + diff) / 2
    options.append((index, fuel_cost))

print(f"Option with the minimal fuel cost is {min(options, key=lambda t: t[1])}")

# Parse data
with open('data.txt') as f:
    data = [int(x) for x in f.readlines()[0].split(',')]
    data.sort()
max_num = max(data)
options = []

for index in range(0, max_num+1):
    # calculate fuel costs of moving all elements to the current index.
    fuel_cost = 0
    for position in data:
        fuel_cost += abs(index-position)
    options.append((index, fuel_cost))


# Option with minimum fuel cost:
print(min(options, key=lambda t: t[1]))

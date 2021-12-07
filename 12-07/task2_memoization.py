cashed_results = {}


def calc_costs(i):
    """Memoization of the function to store results and not have to calculate them multiple times. """
    global cashed_results
    if i not in cashed_results:
        cashed_results[i] = ((i**2) + i) / 2
    return cashed_results[i]


# Parse data
with open('data.txt') as f:
    data = [int(x) for x in f.readlines()[0].split(',')]
    data.sort()
max_num = max(data)
options = {}

# calculate fuel costs of moving all elements to the current index position.
for index in range(0, max_num+1):
    fuel_cost = 0
    for position in data:
        fuel_cost += calc_costs(abs(index-position))
    options[index] = fuel_cost

# Option with minimum fuel cost:
min_key = min(options.keys(), key=(lambda k: options[k]))
print(options[min_key])

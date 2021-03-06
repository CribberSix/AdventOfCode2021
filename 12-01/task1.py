import csv
import more_itertools as it

with open("data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    data = [int(x[0]) for x in list(reader)]

increment = 0
for x, y in it.pairwise(data):
    if x < y:
        increment += 1
print(increment)

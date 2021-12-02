import csv
import more_itertools as it

with open("c:/coding/repositories/AdventOfCode2021/2021-12-01/data.csv") as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    data = [int(x[0]) for x in list(reader)]

increment = 0
prev_sum = None
for t in it.triplewise(data):
    if prev_sum is not None and sum(t) > prev_sum:
        increment += 1
    prev_sum = sum(t)

print(increment)

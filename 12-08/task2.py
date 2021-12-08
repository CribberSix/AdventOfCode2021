from Solver import Solver

# Parse data
with open("data.txt") as f:
    data = [x[:-1].split(' | ') for x in f.readlines()]
    data = [[row[0].split(' '), row[1].split(' ')] for row in data]

all_output_values = []
for row in data:
    # create new Solver instance for each row as they are independent.
    solver = Solver()

    # interpret segments
    for element in row[0]:
        res = solver.interpret_segment(element)

    # reduce possible values until only 1 value is left for each segment.
    solver.clean_solutions()

    # decode output values
    output_values = []
    for element in row[1]:
        output_values.append(solver.decode(element))

    # sum the output values.
    integer_value = int(''.join([str(x) for x in output_values]))
    all_output_values.append(integer_value)

print(f"Sum of all output values is {sum(all_output_values)}.")

from typing import List
import regex as re

data_raw = []
folds_raw = []
switch = False
with open("data.txt") as f:
    for line in f.readlines():
        if line.strip() == "":
            switch = True
        elif switch:
            folds_raw.append(line.strip())  # fold-lines
        else:
            data_raw.append(list(map(int, line.strip().split(','))))  # map coordinate lines

# Parse the folds
folds = []
for fold in folds_raw:
    x = re.search(r'fold along (\w)=(\d+)', fold)
    folds.append((x.group(1), int(x.group(2))))

# Create the sheet of paper
# size of the paper is dependent on the initial fold-points on each axis as max(x)
max_x = [f for f in folds if f[0] == 'x'][0][1] * 2 + 1  # first x-fold point -> * 2 +1 for the fold itself
max_y = [f for f in folds if f[0] == 'y'][0][1] * 2 + 1  # first y-fold point -> * 2 +1  for the fold itself

print(f"The initial paper is {max_y} by {max_x}.")
paper = [[' ' for _ in range(max_x)] for line in range(max_y)]
for dx, dy in data_raw:
    paper[dy][dx] = '█'


def fold_paper(paper: List[str], axis: str, index: int) -> List[str]:
    if axis == 'y':
        # fold along y-axis. Fold rows over rows.
        result = paper[:index]
        reversed_rest = paper[index+1:][::-1]
    elif axis == 'x':
        # fold along x-axis. Fold each row in itself.
        result = [line[:index] for line in paper]
        reversed_rest = [line[index+1:][::-1] for line in paper]
    else:
        raise ValueError("Invalid string-representation of the axis.")

    for y, line in enumerate(result):
        for x, element in enumerate(line):
            result[y][x] = '█' if reversed_rest[y][x] == '█' else result[y][x]
    return result


for axis, index in folds:
    paper = fold_paper(paper, axis, index)
    dots = sum([sum([1 for element in row if element == '█']) for row in paper])
    print(f"Folded along the {axis} axis on index {index}. {dots} dots remaining. Paper size is now ({len(paper)}x{len(paper[0])}).")

for line in paper:
    print(''.join(line))


from task1 import check_line


def get_points(character: str) -> int:
    """Calculates the points for part 2."""
    if character == '(': return 1
    if character == '[': return 2
    if character == '{': return 3
    if character == '<': return 4
    raise ValueError(f"Unknown character '{character}' encountered.")


# Parse data
with open("data.txt") as f:
    data = [x[:-1] for x in f.readlines()]

# Filter to the incomplete lines
checked_lines = []
for line in data:
    checked_lines.append(check_line(line))
incomplete_lines = [x[2] for x in checked_lines if x[0]]

# calculate line score for each incomplete line
line_scores = []
for incomplete_line in incomplete_lines:
    line_score = 0
    for char in incomplete_line[::-1]:
        line_score = (line_score * 5) + get_points(char)
    line_scores.append(line_score)

line_scores.sort()
print(f"Median line score is {line_scores[int(len(line_scores)/2)]}.")

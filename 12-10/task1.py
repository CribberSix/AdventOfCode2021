def give_pendant(character: str) -> str:
    """Returns the pendant to each character."""
    if character == ')': return '('
    if character == ']': return '['
    if character == '}': return '{'
    if character == '>': return '<'
    raise ValueError(f"Unknown character '{character}' encountered.")


def check_line(line: str) -> (bool, str, str):
    """
    Goes through each character to determine whether the line is corrupted or incomplete by building up a stack
    and removing characters from it whenever a matching closing bracket is encountered for the last opened character.

    Accepts a line from the puzzle input.

    Returns a triple:
        - boolean value identifying a line as incomplete. (False => corrupted)
        - string value identifying the corrupted character (if there is one, otherwise None)
        - string value identifying the remaining characters (if there are any, otherwise None)
    """
    opened = ""
    for char in line:
        if char in '([{<':
            opened += char
        elif char in ')]}>':
            if give_pendant(char) == opened[-1]:
                # Found match of last opened symbol -> remove it from the stack
                opened = opened[:-1]
            else:
                # Found corrupted character -> return with the character.
                return False, char, None
        else:
            raise ValueError(f"Unknown character '{char}' encountered.")
    return True, None, opened


def calculate_points(character: str) -> int:
    """Calculates the points for part 1."""
    if character == ')': return 3
    if character == ']': return 57
    if character == '}': return 1197
    if character == '>': return 25137
    raise ValueError(f"Unknown character '{character}' encountered.")


# the __name__ check allows us to import the functions in part2 without executing the code on import.
if __name__ == "__main__":
    with open("data.txt") as f:
        data = [x[:-1] for x in f.readlines()]

    line_results = [check_line(line) for line in data]

    points = [calculate_points(x[1]) for x in line_results if not x[0]]
    print(sum(points))

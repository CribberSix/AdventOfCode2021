def execute_cycle(template: str) -> str:
    """Tries to find a matching rule for each pair of letters in the template.
    Inserts the new polymer letter of the rule between the matching letters.
    """
    new_template = ""
    for index, letter in enumerate(template):
        new_template += letter
        if index < len(template)-1:
            new_template += rules[letter + template[index+1]]
    return new_template


def calculate_solution(template: str) -> int:
    """Calculate occurrences of the letters. Subtract the most common letter occurrences from the least common. """
    d = {x: template.count(x) for x in list(set(template))}
    return d[max(d, key=d.get)] - d[min(d, key=d.get)]


# Parse data
with open("data.txt") as f:
    data = [line.strip().split(" -> ") for line in f.readlines() if line.strip() != ""]
    polymer_template = data[0][0]
    rules = {key: value for key, value in data[1:]}

# Calculate transformation cycles
for i in range(10):
    polymer_template = execute_cycle(polymer_template)
    print(f"After {i+1} steps the new template has a length of {len(polymer_template)} and is: {polymer_template}.")

print("solution_part1", calculate_solution(polymer_template))

from collections import Counter

# The dictionary saves for each key (= combination of level, first_letter, second_letter)
# the number of letter-occurences on the max-level.
memoization = {}


def get_num_of_letters(first_letter, second_letter, current_level, max_level=40):
    """
    Recursively dives down to the maxlevel to calculate the resulting letters.
    Returns the number of letters on the max level as a dict.

    Uses memoization: stores the resulting number of letters for each combination of level, first & second letter.
    If another same combination is encountered, we don't have to traverse down to level 40, but can call on our
    saved value.
    """
    global occurrences, memoization
    if (current_level, first_letter, second_letter) in memoization:
        # no nb
        return memoization[(current_level, first_letter, second_letter)]
    else:
        if current_level == max_level:
            memoization[(current_level, first_letter, second_letter)] = {first_letter: 1}
            return {first_letter: 1}
        else:
            inserted_letter = rules[first_letter + second_letter]
            occ1 = get_num_of_letters(first_letter, inserted_letter, current_level+1, max_level)
            occ2 = get_num_of_letters(inserted_letter, second_letter, current_level+1, max_level)
            combined_occs = dict(Counter(occ1) + Counter(occ2))
            memoization[(current_level, first_letter, second_letter)] = combined_occs
            return combined_occs


# Parse data
with open("data.txt") as f:
    data = [line.strip().split(" -> ") for line in f.readlines() if line.strip() != ""]
    polymer_template = data[0][0]
    rules = {key: value for key, value in data[1:]}
    occurrences = {value: 0 for key, value in data[1:]}

# Calculate the polymer
level_limit = 40
for i, letter in enumerate(polymer_template):
    if i+1 < len(polymer_template):
        # get the number of letters and combine the counts for all pairs in the original template.
        occ = get_num_of_letters(letter, polymer_template[i+1], 0, level_limit)
        occurrences = dict(Counter(occurrences) + Counter(occ))
    else:
        # Add the last letter manually to the count as it is not added by the recursive algorithm.
        occurrences[letter] += 1


print(occurrences)
sol = occurrences[max(occurrences, key=occurrences.get)] - occurrences[min(occurrences, key=occurrences.get)]
print("solution_part2:", sol)

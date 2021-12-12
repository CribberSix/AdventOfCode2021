from typing import List
from copy import copy


def get_neighbours(current_node: str) -> List[str]:
    """
    Get all neighbours for the current node which are not 'start'.
    All paths can be traversed in both ways.
    """
    global links
    return [n2 for n1, n2 in links if n1 == current_node and n2 != 'start'] + \
           [n1 for n1, n2 in links if n2 == current_node and n1 != 'start']


def get_path(current_node: str, current_path: List[str] = [], visited_twice: bool = False) -> None:
    """
    Recursive function to traverse all possible paths.

    Each function call keeps track of
     - their own path,
     - the current node and
     - whether a small cave has been visited twice already.

    For each valid neighbour, the function calls itself to create a new path until it hits 'end' or does not have
    any valid neighbours anymore.
    """
    global valid_paths
    current_path.append(current_node)

    if current_node == 'end':
        valid_paths.append(current_path)
        return

    # check for valid neighbours.
    neighbours = get_neighbours(current_node)
    # Exclude all small caves which were already visited if we have already visited a small cave twice.
    for n in neighbours[:]:
        if visited_twice and n.islower() and n in current_path:
            neighbours.remove(n)

    # For all remaining neighbours, call function to split into individual paths with their own current_paths.
    # Set 'visited_twice' to True if it has already been so, or if the new neighbour is already in the path.
    for neighbour in neighbours:
        get_path(neighbour, copy(current_path), visited_twice or (neighbour.islower() and neighbour in current_path))


with open("data.txt") as f:
    links = [r[:-1].split('-') for r in f.readlines()]

valid_paths = []
get_path("start")

print(len(valid_paths))
print(99138) # solution

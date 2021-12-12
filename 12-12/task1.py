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


def get_path(current_node: str, path: List[str]=[]) -> None:
    """
    Recursive function to traverse all possible paths.

    Each function call keeps track of
     - their own path and
     - the current node.

    For each valid neighbour, the function calls itself to create a new path until it hits 'end' or does not have
    any valid neighbours anymore.
    """
    global valid_paths
    path.append(current_node)

    if current_node == 'end':
        valid_paths.append(path)
        return

    # check for valid neighbours and exclude small caves which were already visited.
    neigbours = get_neighbours(current_node)
    for n in neigbours[:]:
        if n.islower() and n in path:
            neigbours.remove(n)

    # For all remaining neighbours, call function to split into individual paths with their own current_paths.
    for neigbour in neigbours:
        get_path(neigbour, copy(path))


with open("data.txt") as f:
    links = [r[:-1].split('-') for r in f.readlines()]
valid_paths = []
get_path("start")

print(len(valid_paths))

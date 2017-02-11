# Function, shortest_path_search, that generalizes the search algorithm.
# This function should have three inputs, a start state,
# a successors function, and an is_goal function.


def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()  # set of states we have visited
    frontier = [[start]]  # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []


# --------------
# Example problem
#
# Let's say the states in an optimization problem are given by integers.
# From a state, i, the only possible successors are i+1 and i-1. Given
# a starting integer, find the shortest path to the integer 8.
#
# This is an overly simple example of when we can use the
# shortest_path_search function. We just need to define the appropriate
# is_goal and successors functions.

def is_goal(state):
    if state == 8:
        return True
    else:
        return False


def successors(state):
    successors = {state + 1: '->',
                  state - 1: '<-'}
    return successors


# test
assert shortest_path_search(5, successors, is_goal) == [5, '->', 6, '->', 7, '->', 8]

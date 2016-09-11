import doctest

def pour_problem(X, Y, goal, start=(0, 0)):
    """X and Y are the capacity of glasses; (x,y) is current fill levels
    and represents a state. The goal is a level that can be in either glass.
    Start at start state and follow successors until we reach the goal.
    Keep track of frontier and previously explored; fail when no frontier."""
    if goal in start:
        return [start]
    explored = set()        # set of states we have visited
    frontier = [[start]]    # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        (x, y) = path[-1]   # last state in the first path of the frontier
        for (state, action) in successors(x, y, X, Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return Fail

Fail = []


def successors(x, y, X, Y):
    """Return a dictionary of {state:action} pairs describing what can be
    reached from the (x,y) state, and how"""
    assert x <= X and y <= Y  # (x, y) is glass levels; X and Y are glass sizes
    return {((0, y+x) if y+x <= Y else (x-(Y-y), y+(Y-y))): 'X->Y',
            ((x+y, 0) if x+y <= X else (x+(X-x), y-(X-x))): 'X<-Y',
            (X, y): 'fill X',
            (x, Y): 'fill Y',
            (0, y): 'empty X',
            (x, 0): 'empty Y'}


class Test: """
>>> successors(0, 0, 4, 9)
{(0, 9): 'fill Y', (0, 0): 'empty Y', (4, 0): 'fill X'}

>>> pour_problem(4, 9, 6)
[(0, 0), 'fill Y', (0, 9), 'X<-Y', (4, 5), 'empty X', (0, 5), 'X<-Y', (4, 1), 'empty X', (0, 1), 'X<-Y', (1, 0), 'fill Y', (1, 9), 'X<-Y', (4, 6)]
    """

# print(pour_problem(4, 9, 5))
# print(pour_problem(4, 9, 6))
# print(successors(0, 0, 4, 9))
# print(successors(3, 5, 4, 9))
# print(successors(3, 7, 4, 9))
print(doctest.testmod())
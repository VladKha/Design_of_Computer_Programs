import doctest

''' Not efficient solving'''

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and
    '<-' for there to here."""
    here, there, t = state
    result = {}
    light = 'light'

    def move(a, b, direction):
        for i in a:
            if i is not light:
                for j in a:
                    if j is not light:
                        a_tmp, b_tmp = (a - frozenset([i, j, light]), b | frozenset([i, j, light]))
                        if direction == '->':
                            new_state = (frozenset(a_tmp), frozenset(b_tmp), t + max(i, j))
                        else:
                            new_state = (frozenset(b_tmp), frozenset(a_tmp), t + max(i, j))
                        result[new_state] = (i, j, direction)

    if light in here:
        move(here, there, '->')
    else:
        move(there, here, '<-')
    return result


def path_states(path):
    """Return a list of states in this path."""
    return path[0::2]


def path_actions(path):
    """Return a list of actions in this path."""
    return path[1::2]


def bridge_problem(here):
    """Find the fastest (least elapsed time) path to the goal in the bridge problem."""
    here = frozenset(here) | frozenset(['light'])
    explored = set()    # set of states we have visited
    # State will be a (people_here, people_there, time_elapsed)
    frontier = [[(here, frozenset(), 0)]]   # ordered list of paths we have blazed
    if not here:
        return frontier[0]
    while frontier:
        path = frontier.pop(0)
        here1, there1, t1 = path[-1]
        if not here1 or here1 == set('light'):      # check for solution when we pull best path
            return path
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                frontier.append(path2)
                frontier.sort(key=elapsed_time)
    return Fail
Fail = [(frozenset(), frozenset(), 0)]


def elapsed_time(path):
    return path[-1][2]


''' Tests '''

def test():
    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {
                (frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) == {
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}

    testpath = [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
                (5, 2, '->'),                                        # action 1
                (frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
                (2, 1, '->'),                                        # action 2
                (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
                (5, 5, '->'),
                (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
                (5, 10, '->'),
                (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
                (2, 2, '->'),
                (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
                (10, 1, '->'),
                (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
                (10, 10, '->'),
                (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
                (10, 2, '->'),
                (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
                (5, 1, '->'),
                (frozenset([2, 10, 5]), frozenset([1, 'light']), 1),
                (1, 1, '->')]
    assert path_states(testpath) == [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
                (frozenset([10, 5]), frozenset([1, 2, 'light']), 2),                      # state 2
                (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
                (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
                (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
                (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
                (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
                (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
                (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
                (frozenset([2, 10, 5]), frozenset([1, 'light']), 1)]
    assert path_actions(testpath) == [(5, 2, '->'), # action 1
                                      (2, 1, '->'), # action 2
                                      (5, 5, '->'),
                                      (5, 10, '->'),
                                      (2, 2, '->'),
                                      (10, 1, '->'),
                                      (10, 10, '->'),
                                      (10, 2, '->'),
                                      (5, 1, '->'),
                                      (1, 1, '->')]

    assert bridge_problem(frozenset((1, 2)))[-1][-1] == 2  # the [-1][-1] grabs the total elapsed time
    assert bridge_problem(frozenset((1, 2, 5, 10)))[-1][-1] == 17

    return 'tests pass'


class TestBridge: """
>>> elapsed_time(bridge_problem([1,2,5,10]))
17

## There are two equally good solutions
>>> S1 = [(2, 1, '->'), (1, 1, '<-'), (5, 10, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> S2 = [(2, 1, '->'), (2, 2, '<-'), (5, 10, '->'), (1, 1, '<-'), (2, 1, '->')]
>>> path_actions(bridge_problem([1,2,5,10])) in (S1, S2)
True

## Try some other problems
>>> path_actions(bridge_problem([1,2,5,10,15,20]))
[(2, 1, '->'), (1, 1, '<-'), (10, 5, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (15, 20, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> path_actions(bridge_problem([1,2,4,8,16,32]))
[(2, 1, '->'), (1, 1, '<-'), (8, 4, '->'), (2, 2, '<-'), (1, 2, '->'), (1, 1, '<-'), (16, 32, '->'), (2, 2, '<-'), (2, 1, '->')]

>>> [elapsed_time(bridge_problem([1,2,4,8,16][:N])) for N in range(6)]
[0, 1, 2, 7, 15, 28]

# >>> [elapsed_time(bridge_problem([1,1,2,3,5,8,13,21][:N])) for N in range(8)]
[0, 1, 1, 2, 6, 12, 19, 30]

"""

print(doctest.testmod())

print(test())
print(bridge_problem([1, 2, 5, 10]))
print(bridge_problem([1, 2, 5, 10])[1::2])
print(bridge_problem([1, 2, 5, 10])[-1][-1])

print()

people = [1, 2, 4, 8, 16]
print([elapsed_time(bridge_problem(people[:N])) for N in range(len(people) + 1)])
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings:
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C', '<-CC'
# where 'MM->' means two missionaries travel to the right side.

Fail = []


def mc_problem(start=(3, 3, 1, 0, 0, 0), goal=None):
    if goal is None:
        goal = (0, 0, 0) + start[:3]
    if start == goal:
        return [start]
    explored = set()    # set of states we have visited
    frontier = [[start]]    # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in csuccessors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if state == goal:
                    return path2
                else:
                    frontier.append(path2)
    return Fail


def csuccessors(state):
    """
    Takes a state as input and returns a dictionary of {state:action} pairs
    """
    M1, C1, B1, M2, C2, B2 = state
    if M1 < C1 or M2 < C2:
        return {}

    result = {}

    if B1 > 0:
        if C1 >= 1:
            result[(M1, C1 - 1, 0, M2, C2 + 1, 1)] = 'C->'
        if C1 >= 2:
            result[(M1, C1 - 2, 0, M2, C2 + 2, 1)] = 'CC->'
        if M1 >= 1:
            result[(M1 - 1, C1, 0, M2 + 1, C2, 1)] = 'M->'
        if M1 >= 2:
            result[(M1 - 2, C1, 0, M2 + 2, C2, 1)] = 'MM->'
        if M1 >= 1 and C1 >= 1:
            result[(M1 - 1, C1 - 1, 0, M2 + 1, C2 + 1, 1)] = 'MC->'

    if B2 > 0:
        if C2 >= 1:
            result[(M1, C1 + 1, 1, M2, C2 - 1, 0)] = '<-C'
        if C2 >= 2:
            result[(M1, C1 + 2, 1, M2, C2 - 2, 0)] = '<-CC'
        if M2 >= 1:
            result[(M1 + 1, C1, 1, M2 - 1, C2, 0)] = '<-M'
        if M2 >= 2:
            result[(M1 + 2, C1, 1, M2 - 2, C2, 0)] = '<-MM'
        if M2 >= 1 and C2 >= 1:
            result[(M1 + 1, C1 + 1, 1, M2 - 1, C2 - 1, 0)] = '<-MC'

    return result


def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->',
                                               (1, 2, 0, 1, 0, 1): 'M->',
                                               (0, 2, 0, 2, 0, 1): 'MM->',
                                               (1, 1, 0, 1, 1, 1): 'MC->',
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C',
                                               (2, 1, 1, 3, 3, 0): '<-M',
                                               (3, 1, 1, 2, 3, 0): '<-MM',
                                               (1, 3, 1, 4, 1, 0): '<-CC',
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print(test())

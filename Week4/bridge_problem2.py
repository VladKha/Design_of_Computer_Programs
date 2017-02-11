
def bsuccessors2(state):
    """Return a dict of {state:action} pairs. A state is a
    (here, there) tuple, where here and there are frozensets
    of people (indicated by their travel times) and/or the light."""
    here, there = state
    result = {}
    light = 'light'

    def move(a, b, direction):
        for i in a:
            if i is not light:
                for j in a:
                    if j is not light:
                        a_tmp, b_tmp = (a - frozenset([i, j, light]), b | frozenset([i, j, light]))
                        if direction == '->':
                            new_state = (frozenset(a_tmp), frozenset(b_tmp))
                        else:
                            new_state = (frozenset(b_tmp), frozenset(a_tmp))
                        result[new_state] = (i, j, direction)

    if light in here:
        move(here, there, '->')
    else:
        move(there, here, '<-')
    return result


def path_cost(path):
    """The total cost of a path (which is stored in a tuple
    with the final action."""
    # path = (state, (action, total_cost), state, ... )
    if len(path) < 3:
        return 0
    else:
        action, total_cost = path[-2]
        return total_cost


def bcost(action):
    """Returns the cost (a number) of an action in the
    bridge problem."""
    # An action is an (a, b, arrow) tuple; a and b are
    # times; arrow is a string.
    a, b, arrow = action
    return max(a, b)


def test():
    here1 = frozenset([1, 'light'])
    there1 = frozenset([])

    here2 = frozenset([1, 2, 'light'])
    there2 = frozenset([3])

    assert bsuccessors2((here1, there1)) == {
            (frozenset([]), frozenset([1, 'light'])): (1, 1, '->')}
    assert bsuccessors2((here2, there2)) == {
            (frozenset([1]), frozenset(['light', 2, 3])): (2, 2, '->'),
            (frozenset([2]), frozenset([1, 3, 'light'])): (1, 1, '->'),
            (frozenset([]), frozenset([1, 2, 3, 'light'])): (2, 1, '->')}

    assert path_cost(('fake_state1', ((2, 5, '->'), 5), 'fake_state2')) == 5
    assert path_cost(('fs1', ((2, 1, '->'), 2), 'fs2', ((3, 4, '<-'), 6), 'fs3')) == 6
    assert bcost((4, 2, '->'), ) == 4
    assert bcost((3, 10, '<-'), ) == 10

    return 'tests pass'

print(test())

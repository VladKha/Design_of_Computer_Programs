# -----------------
# User Instructions
#
# write a function, bsuccessors2 that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# The new representation for a path should be a list of
# [state, (action, total time), state, ... , ], though this
# function will just return {state:action} pairs and will
# ignore total time.
#
# The previous bsuccessors function is included for your reference.

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
    return 'tests pass'

print(test())
# -----------------
# User Instructions
#
# Write the two action functions, hold and roll. Each should take a
# state as input, apply the appropriate action, and return a new
# state.
#
# States are represented as a tuple of (p, me, you, pending) where
# p:       an int, 0 or 1, indicating which player's turn it is.
# me:      an int, the player-to-move's current score
# you:     an int, the other player's current score.
# pending: an int, the number of points accumulated on current turn, not yet scored


def hold(state):
    """Apply the hold action to a state to yield a new state:
    Reap the 'pending' points and it becomes the other player's turn."""
    (p, me, you, pending) = state
    return (other[p], you, me + pending, 0)


def roll(state, d):
    """Apply the roll action to a state (and a die roll d) to yield a new state:
    If d is 1, get 1 point (losing any accumulated 'pending' points),
    and it is the other player's turn. If d > 1, add d to 'pending' points."""
    (p, me, you, pending) = state
    if d == 1:
        return (other[p], you, me + 1, 0)   # pig out; other's player turn
    else:
        return (p, me, you, pending + d)    # accumulate die roll in pending


other = {1: 0, 0: 1}    # mapping from player to other player


def test():
    assert hold((1, 10, 20, 7)) == (0, 20, 17, 0)
    assert hold((0, 5, 15, 10)) == (1, 15, 15, 0)
    assert roll((1, 10, 20, 7), 1) == (0, 20, 11, 0)
    assert roll((0, 5, 15, 10), 5) == (0, 5, 15, 15)
    return 'tests pass'


print(test())


# -----------------
# User Instructions
#
# Write a strategy function, clueless, that ignores the state and
# chooses at random from the possible moves (it should either
# return 'roll' or 'hold'). Take a look at the random library for
# helpful functions.

import random

possible_moves = ['roll', 'hold']


def clueless(state):
    """A strategy that ignores the state and chooses at random from possible moves."""
    return random.choice(possible_moves)

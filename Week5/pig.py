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


# -----------------
# User Instructions
#
# In this problem, you will complete the code for the hold_at(x)
# function. This function returns a strategy function (note that
# hold_at is NOT the strategy function itself). The returned
# strategy should hold if and only if pending >= x or if the
# player has reached the goal.

goal = 50


def hold_at(x):
    """Return a strategy that holds if and only if
    pending >= x or player reaches goal."""
    def strategy(state):
        (p, me, you, pending) = state
        return 'hold' if (pending >= x or me + pending >= goal) else 'roll'
    strategy.__name__ = 'hold_at(%d)' % x
    return strategy


def test():
    assert hold_at(30)((1, 29, 15, 20)) == 'roll'
    assert hold_at(30)((1, 29, 15, 21)) == 'hold'
    assert hold_at(15)((0, 2, 30, 10))  == 'roll'
    assert hold_at(15)((0, 2, 30, 15))  == 'hold'
    return 'tests pass'

print(test())


# -----------------
# User Instructions
#
# Write a function, play_pig, that takes two strategy functions as input,
# plays a game of pig between the two strategies, and returns the winning
# strategy. Enter your code at line 41.
#
# You may want to borrow from the random module to help generate die rolls.


def dierolls():
    """Generate die rolls"""
    while True:
        yield random.randint(1, 6)


def play_pig(A, B, dierolls=dierolls()):
    """Play a game of pig between two players, represented by their strategies.
    Each time through the main loop we ask the current player for one decision,
    which must be 'hold' or 'roll', and we update the state accordingly.
    When one player's score exceeds the goal, return that player."""
    strategies = [A, B]
    state = (0, 0, 0, 0)
    while True:
        (p, me, you, pending) = state
        if me >= goal:
            return strategies[p]
        elif you >= goal:
            return strategies[other[p]]

        action = strategies[p](state)
        if action == 'hold':
            state = hold(state)
        elif action == 'roll':
            state = roll(state, next(dierolls))


def always_roll(state):
    return 'roll'


def always_hold(state):
    return 'hold'


def test():
    for _ in range(10):
        winner = play_pig(always_hold, always_roll)
        assert winner.__name__ == 'always_roll'

    A, B = hold_at(50), clueless
    rolls = iter([6] * 9)
    assert play_pig(A, B, rolls) == A
    return 'tests pass'


print(test())

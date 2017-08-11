import itertools
from fractions import Fraction


sex = 'BG'


def product(*variables):
    """The cartesian product (as a str) of the possibilities for ach variable."""
    print(type(variables))
    return list(map(''.join, itertools.product(*variables)))


two_kids = product(sex, sex)

print(two_kids)

one_boy = [s for s in two_kids if 'B' in s]


def two_boys(s):
    return s.count('B') == 2


def condP(predicate, event):
    """Conditional probability: P(predicate(s) | s in event).
    The proportion of states in event for whuch predicate is true."""
    pred = [s for s in event if predicate(s)]
    return Fraction(len(pred), len(event))

print(condP(two_boys, one_boy))


"""
Out of all families with two kids with at least one boy born on a Tuesday,
what is the probability of two boys?
"""
day = 'SMTWtFs'

two_kids_birthdays = product(sex, day, sex, day)
print(two_kids_birthdays)

boy_tuesday = [s for s in two_kids_birthdays if 'BT' in s]
print(condP(two_boys, boy_tuesday))

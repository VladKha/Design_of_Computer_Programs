def ints(start, end=None):
    """Generates integers from 'start' to 'end' or infinitely if 'end' is None"""
    i = start
    while end is None or i <= end:
        yield i
        i += 1


def all_ints():
    """Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."""
    yield 0
    for i in ints(1):
        yield +i
        yield -i


c = 0
g = all_ints()
while c <= 100:
    print(next(g))
    c += 1

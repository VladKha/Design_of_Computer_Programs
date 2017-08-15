import itertools
import time


def imright(h1, h2):
    """House h1 is immediately right of h2 if h1-h2 == 1."""
    return h1 - h2 == 1


def next_to(h1, h2):
    """Two houses are next to each other if they differ by 1."""
    return abs(h1 - h2) == 1


def zebra_puzzle():
    """Return a tuple (WATER, ZEBRA) indicating their house numbers."""
    debug = Debugger()
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))  # 1
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in debug.c(orderings)
                if imright(green, ivory)        # 6
                for (Englishman, Spaniard, Ukrainian, Japanese, Norwegian) in debug.c(orderings)
                if Englishman is red            # 2
                if Norwegian is first           # 10
                if next_to(Norwegian, blue)     # 15
                for (coffee, tea, milk, oj, WATER) in debug.c(orderings)
                if coffee is green              # 4
                if Ukrainian is tea             # 5
                if milk is middle               # 9
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in debug.c(orderings)
                if Kools is yellow              # 8
                if LuckyStrike is oj            # 13
                if Japanese is Parliaments      # 14
                for (dog, snails, fox, horse, ZEBRA) in debug.c(orderings)
                if Spaniard is dog              # 3
                if OldGold is snails            # 7
                if next_to(Chesterfields, fox)  # 11
                if next_to(Kools, horse)        # 12
                )


def timed_call(fn, *args):
    """Call function with args; return the time in seconds and result."""
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result


def average(numbers):
    """Return the average (arithmetic mean) of a sequence of numbers."""
    return sum(numbers) / float(len(numbers))


def timed_calls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timed_call(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        start = time.clock()
        while time.clock() - start <= n:
            times.append(timed_call(fn, *args)[0])
    return min(times), average(times), max(times)


def instrument_fn(fn, *args):
    c = Debugger()
    result = fn(*args)
    print('{} got {} with {} iters over {} items'.format(fn.__name__, result, c.starts, c.items))


class Debugger:
    starts = 0
    items = 0

    def __init__(self):
        Debugger.starts, Debugger.items = 0, 0

    @staticmethod
    def c(sequence):
        """Generate items in sequence; keeping counts as we go. c.starts is
        the number of sequenced started; c.items is number of items generated."""
        Debugger.starts += 1
        for item in sequence:
            Debugger.items += 1
            yield item


print(timed_calls(10, zebra_puzzle))
instrument_fn(zebra_puzzle)

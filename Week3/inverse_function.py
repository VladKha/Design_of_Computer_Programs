# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the
# non-negative numbers. The runtime of your program should be
# proportional to the LOGARITHM of the input. You may want to
# do some research into binary search and Newton's method to
# help you out.
#
# This function should return another function which computes the
# inverse of the input function.
#
# Your inverse function should also take an optional parameter,
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is
# efficient enough.



def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1


# my solution
def inverse1(f, delta = 1/1000.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        lo = 0
        hi = y
        # counter = 0
        while True:
            # counter += 1
            x = (hi + lo) / 2.
            if hi - lo <= delta:
                # print(counter)
                return x
            if f(x) < y:
                lo = x
            else:
                hi = x
    return f_1


# Peter Norvig's solution
def inverse2(f, delta = 1/1000.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        lo, hi = find_bounds(f, y)
        return binary_search(f, y, lo, hi, delta)
    return f_1

def find_bounds(f, y):
    x = 1.
    # counter = 0
    while f(x) < y:
        x *= 2
        # counter += 1
    lo = 0 if (x == 1) else x / 2
    # print(counter, '+ ', end='')
    return lo, x

def binary_search(f, y, lo, hi, delta):
    # counter = 0
    while lo <= hi:
        # counter += 1
        x = (hi + lo) / 2.
        if f(x) < y:
            lo = x + delta
        elif f(x) > y:
            hi = x - delta
        else:
            # print(counter)
            return x
    # print(counter)
    return hi if (f(hi)-y < y-f(lo)) else lo


def square(x): return x*x
sqrt = slow_inverse(square)
sqrt1 = inverse1(square)
sqrt2 = inverse2(square)

import math
# print("Real sqrt = ", end='')
print(math.sqrt(100000000000), end="\n\n")

# print("My solution:\nsteps = ", end='')
print(sqrt1(100000000000), end="\n\n")

# print("Peter Norvig's solution:\nsteps = ", end='')
print(sqrt2(100000000000))

# print("Slow initial sqrt:", end='')
print(sqrt(100000000000))
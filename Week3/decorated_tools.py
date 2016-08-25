from functools import update_wrapper

def decorator(d):
    """Make function d a decorator: d wraps a function fn."""
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d

# def decorator(d):             # alternative definition
#     return lambda fn: update_wrapper(d(fn), fn)
# decorator = decorator(decorator)

@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with the same args, we can just look it up."""
    cache = {}

    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some elements of args can't be a dict key
            return f(args)
    return _f


@decorator
def count_calls(f):
    """Decorator that makes the function count calls to it, in callcounts[f]."""
    def _f(*args):
        calls_count_map[_f] += 1
        return f(*args)
    calls_count_map[_f] = 0
    return _f

calls_count_map = {}


@decorator
def trace(f):
    indent = '   '
    def _f(*args):
        signature = '%s(%s)' % (f.__name__, ', '.join(map(repr, args)))
        print('%s--> %s' % (trace.level*indent, signature))
        trace.level += 1
        try:
            result = f(*args)
            print('%s<-- %s == %s' % ((trace.level-1)*indent,
                                      signature, result))
        finally:
            trace.level -= 1
        return result
    trace.level = 0
    return _f



def disabled(f):
    """Function to disable any decorator function"""
    return f
# trace = disabled


@count_calls
@trace
@memo
def fib(n):
    return 1 if n <= 1 else fib(n - 1) + fib(n - 2)


# --------------------------------------------------- Testing ----------------------------------------------------------
# print("n \t fib(n) \t calls")
# for n in range(31):
#     print("{} \t {} \t\t {}".format(n, fib(n), calls_count_map[fib]))
#     calls_count_map[fib] = 0


print(fib(30))

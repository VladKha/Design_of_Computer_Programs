

def lit(s):
    set_s = set([s])       # little optimization to execute this line only once, but not every time constructing pattern
    return lambda Ns: set_s if len(s) in Ns else null
def alt(x, y):      return lambda Ns: x(Ns) | y(Ns)
def star(x):        return lambda Ns: opt(plus(x))(Ns)
def plus(x):        return lambda Ns: genseq(x, star(x), Ns, startx=1) #Tricky
def oneof(chars):
    set_chars = set(chars)
    return lambda Ns: set_chars if 1 in Ns else null
def seq(x, y):      return lambda Ns: genseq(x, y, Ns)
def opt(x):         return alt(epsilon, x)
dot = oneof('?')    # The alphabet can be expanded to more chars.
epsilon = lit('')   # The pattern that matches the empty string.


def genseq(x, y, Ns, startx=0):
    """Set of matches to xy whose total len is in Ns, with x-match's len in Ns"""
    # Tricky part: x+ is defined as: x+ = x x*
    # To stop the recursion, the first x must generate at least 1 char,
    # and the the recursive x* has that many fewer characters. We use
    # startx=1 to say that x must match at least 1 character
    if not Ns:
        return null
    xmatches = x(set(range(startx, max(Ns) + 1)))
    Ns_x = set(len(m) for m in xmatches)
    Ns_y = set(n-m for n in Ns for m in Ns_x if n-m >= 0)
    ymatches = y(Ns_y)
    return set(m1 + m2
               for m1 in xmatches for m2 in ymatches
               if len(m1+m2) in Ns)



null = frozenset([])

def test():

    f = lit('hello')
    assert f(set([1, 2, 3, 4, 5])) == set(['hello'])
    assert f(set([1, 2, 3, 4]))    == null

    g = alt(lit('hi'), lit('bye'))
    assert g(set([1, 2, 3, 4, 5, 6])) == set(['bye', 'hi'])
    assert g(set([1, 3, 5])) == set(['bye'])

    h = oneof('theseletters')
    assert h(set([1, 2, 3])) == set(['t', 'h', 'e', 's', 'l', 'r'])
    assert h(set([2, 3, 4])) == null

    return 'tests pass'

print(test())
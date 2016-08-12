import itertools
import re


# brute forse
def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            print(f)


def fill_in(formula):
    """Generate all possible fillings-in of letters in formula with digits."""
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    """Formula f is valid if and only if it has no
    numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False


solve('YOU == ME**2')







# optimized variant
def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula"""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                result_formula = formula.translate(table)
                print(result_formula)
        except ArithmeticError:
            pass


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as params of function. For example, 'YOU == ME**2' returns
    (lambda Y,M,E,U,O: (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO'.
    The first digit of a multi-digit number can't be 0. So if YOU is a word
    in the formula, and the function is called with Y equal to 0,
    the function should return False."""
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    first_letters = set(re.findall(r'\b([A-Z])[A-Z]', formula))
    params = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)

    if first_letters:
        tests = ' and '.join(L + ' != 0' for L in first_letters)
        body = '{} and {}'.format(tests, body)

    f = 'lambda {}: {}'.format(params, body)

    if verbose:
        print(f)
    return eval(f), letters


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('{}*{}'.format(10 ** i, d))
                 for (i, d) in enumerate(reversed(word))]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


print()
faster_solve('YOU == ME**2')

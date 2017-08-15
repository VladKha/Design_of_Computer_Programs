# -----------------
# User Instructions
#
# In this problem, you will define a function, boggle_words(),
# that takes a board as input and returns a set of words that
# can be made from the board according to the rules of Boggle.


def boggle_words(board, min_length=3):
    """Find all the words on this Boggle board; return as a set of words."""
    N = size(board)
    result = set()

    for (i, L) in enumerate(board):
        if L != BORDER:
            new_board = board[:i] + BORDER + board[i + 1:]
            find_words(L, i, new_board, result, min_length, N)
    return result


def find_words(prefix, prev_index, board, result, min_length, N):
    if len(prefix) >= min_length and prefix in WORDS:
        result.add(prefix)
    if prefix in PREFIXES:
        for i in neighbors(prev_index, N):
            L = board[i]
            if L != BORDER:
                new_board = board[:i] + BORDER + board[i+1:]
                find_words(prefix + L, i, new_board, result, min_length, N)
    return result


def test():
    b = Board('XXXX TEST XXXX XXXX')
    assert b == '|||||||XXXX||TEST||XXXX||XXXX|||||||'
    assert display(b) == """
||||||
|XXXX|
|TEST|
|XXXX|
|XXXX|
||||||""".strip()
    assert boggle_words(b) == {'SET', 'SEX', 'TEST'}
    assert neighbors(20, 6) == (13, 14, 15, 19, 21, 25, 26, 27)
    assert len(boggle_words(Board('TPLER ORAIS METND DASEU NOWRB'))) == 317
    assert boggle_words(Board('PLAY THIS WORD GAME')) == {'LID', 'SIR', 'OAR', 'LIS', 'RAG', 'SAL',
                                                          'RAM', 'RAW', 'SAY', 'RID', 'RIA', 'THO',
                                                          'HAY', 'MAR', 'HAS', 'AYS', 'PHI', 'OIL',
                                                          'MAW', 'THIS', 'LAY', 'RHO', 'PHT',
                                                          'PLAYS', 'ASIDE', 'ROM', 'RIDE', 'ROT',
                                                          'ROW', 'MAG', 'THIRD', 'WOT', 'MORE',
                                                          'WOG', 'WORE', 'SAID', 'MOR', 'SAIL',
                                                          'MOW', 'MOT', 'LAID', 'MOA', 'LAS', 'MOG',
                                                          'AGO', 'IDS', 'HAIR', 'GAME', 'REM',
                                                          'HOME', 'RED', 'WORD', 'WHA', 'WHO',
                                                          'WHOM', 'YID', 'DRAW', 'WAG', 'SRI',
                                                          'TOW', 'DRAG', 'YAH', 'WAR', 'MED',
                                                          'HIRE', 'TOWARDS', 'ORS', 'ALT', 'ORE',
                                                          'SIDE', 'ALP', 'ORA', 'TWA', 'ERS', 'TOR',
                                                          'TWO', 'AIS', 'AIR', 'AIL', 'ERA', 'TOM',
                                                          'AID', 'TOG', 'DIS', 'HIS', 'GAR', 'GAM',
                                                          'HID', 'HOG', 'PLAY', 'GOA', 'HOW', 'HOT',
                                                          'WARM', 'GOT', 'IRE', 'GOR', 'ARS', 'ARM',
                                                          'ARE', 'TOWARD', 'THROW'}
    return 'tests pass'


def Board(text):
    """Input is a string of space-separated rows of N letters each;
    result is a string of size (N+2)**2 with borders all around."""
    rows = text.split()
    N = len(rows)
    rows = [BORDER * N] + rows + [BORDER * N]
    return ''.join(BORDER + row + BORDER for row in rows)


def size(board): return int(len(board) ** 0.5)


def neighbors(i, N):
    return (i - N - 1, i - N, i - N + 1, i - 1, i + 1, i + N - 1, i + N, i + N + 1)


BORDER = '|'


def display(board):
    """Return a string representation of board, suitable for printing."""
    N = size(board)
    return '\n'.join(board[i:i + N] for i in range(0, N ** 2, N))


# ------------
# Helpful functions
#
# You may find the following functions useful. These functions
# are identical to those we defined in lecture.

def prefixes(word):
    """A list of the initial sequences of a word, not including the complete word."""
    return [word[:i] for i in range(len(word))]


def readwordlist(filename):
    """Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"""
    word_set = set()
    prefix_set = set()
    with open(filename, 'r') as fin:
        for line in fin:
            word = line.strip().upper()
            if word:
                word_set.add(word)
                prefix_set.update(prefixes(word))
    return word_set, prefix_set


WORDS, PREFIXES = readwordlist('../words4k.txt')

print(test())

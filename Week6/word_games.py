# -----------------
# User Instructions
#
# Write a function, readwordlist, that takes a filename as input and returns
# a set of all the words and a set of all the prefixes in that file, in
# uppercase. For testing, you can assume that you have access to a file
# called 'words4k.txt'


def prefixes(word):
    """A list of the initial sequences of a word, not including the complete word."""
    return [word[:i] for i in range(len(word))]


def readwordlist(filename):
    """Read the words from a file and return a set of the words
    and a set of the prefixes."""
    word_set = set()
    prefix_set = set()
    with open(filename, 'r') as fin:
        for line in fin:
            word = line.strip().upper()
            if word:
                word_set.add(word)
                prefix_set.update(prefixes(word))
    return word_set, prefix_set


WORDS, PREFIXES = readwordlist('words4k.txt')


def test():
    assert len(WORDS) == 3892
    assert len(PREFIXES) == 6475
    assert 'UMIAQS' in WORDS
    assert 'MOVING' in WORDS
    assert 'UNDERSTANDIN' in PREFIXES
    assert 'ZOMB' in PREFIXES
    return 'tests pass'


print(test())

# -----------------
# User Instructions
#
# Write a function, extend_prefix, nested in find_words,
# that checks to see if the prefix is in WORDS and
# adds that to results if it is.
#
# If not, your function should check to see if the prefix
# is in PREFIXES, and if it is should recursively add letters
# until the prefix is no longer valid.


def find_words(letters, pre='', results=None):
    if results is None:
        results = set()
    if pre in WORDS:
        results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            find_words(letters.replace(L, '', 1), pre + L, results)
    return results

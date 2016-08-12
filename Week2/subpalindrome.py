# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficiency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if text == '':
        return (0, 0)
    s = text.lower()
    i, j = 0, 0
    for start in range(len(s)):
        for end in range(start + 1, start + 3):
            i, j = grow(s, start, end, i, j)
    return (i, j + 1)


def grow(s, begin, end, i, j):
    while end < len(s) and is_palindrome(s[begin:end + 1]):
        if end - begin > j - i:
            i, j = begin, end
        if begin == 0:
            break
        begin -= 1
        end += 1
    return (i, j)


def is_palindrome(s):
    return s == s[::-1]


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print(test())
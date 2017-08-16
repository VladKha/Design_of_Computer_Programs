"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming.
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
import itertools


def logic_puzzle():
    """Return a list of the names of the people, in the order they arrive."""
    days = (monday, tuesday, wednesday, thursday, friday) = (1, 2, 3, 4, 5)
    possible_days = list(itertools.permutations(days))
    return next(
        answer(Wilkes=Wilkes, Hamming=Hamming, Minsky=Minsky, Knuth=Knuth, Simon=Simon)
        for (laptop, droid, tablet, iphone, _) in possible_days
        if wednesday == laptop                                                  # 1
        if friday != tablet                                                     # 8
        if iphone == tuesday or tablet == tuesday                               # 12

        for (programmer, writer, manager, designer, _) in possible_days
        if thursday != designer                                                 # 7
        if designer != droid                                                    # 9

        for (Wilkes, Hamming, Minsky, Knuth, Simon) in possible_days
        if Wilkes != programmer                                                 # 2
        if {droid, programmer} == {Wilkes, Hamming}                             # 3
        if writer != Minsky                                                     # 4
        if manager not in [Knuth, tablet]                                       # 5
        if Knuth == Simon + 1                                                   # 6
        if Knuth == manager + 1                                                 # 10
        if {laptop, Wilkes} == {monday, writer}                                 # 11
    )


def answer(**names):
    """Given a dict of {name:day}, return a list of names sorted by day."""
    return sorted(names, key=lambda name: names[name])

print(logic_puzzle())

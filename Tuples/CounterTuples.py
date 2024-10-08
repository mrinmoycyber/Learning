# Count Frequency of Elements in a Tuple
# Given a tuple of integers, count the frequency of each element.

from collections import Counter

def counter_frequencies(tup):
    return dict(Counter(tup))

my_tuple = (1, 2, 2, 3, 1, 4, 1, 3, 3)
frequency = counter_frequencies(my_tuple)
print(frequency)
# Create an algorithm to efficiently compute the approximate median of a list of numbers.

# More precisely, given an unordered list of N numbers,
# find an element whose rank is between N / 4 and 3 * N / 4,
# with a high level of certainty, in less than O(N) time.


from math import log
from random import sample


def find_median(array, precision):
    m = precision * int(log(len(array), 2))

    subset = sample(array, m)
    subset.sort()

    return subset[m // 2]

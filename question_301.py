# Implement a data structure which carries out the following operations without resizing the underlying array:

# add(value): Add a value to the set of values.
# check(value): Check whether a value is in the set.

# The check method may return occasional false positives (in other words, incorrectly identifying an element as part of the set),
# but should always correctly identify a true element.

import hashlib
from typing import List, Callable


class BloomFilter:
    def __init__(self, size: int = 1000, hash_functions=None):
        self.size = size
        self.bit_array = [0] * size

        # Use sha256 and sha512 as default hash functions if none provided
        if hash_functions is None:
            self.hash_functions = [
                hashlib.sha256,
                hashlib.sha512
            ]
        else:
            self.hash_functions = hash_functions

    def _hash(self, value: str, hash_function: Callable) -> int:
        # Hash the value and return an index in the range of the array size
        hashed = hash_function(str(value).encode('utf-8')).hexdigest()
        return int(hashed, 16) % self.size

    def add(self, value: str) -> None:
        for hash_function in self.hash_functions:
            index = self._hash(value, hash_function)
            self.bit_array[index] = 1

    def check(self, value: str) -> bool:
        for hash_function in self.hash_functions:
            index = self._hash(value, hash_function)
            # If any of the bits are not set, it's definitely not in the set
            if self.bit_array[index] == 0:
                return False
        # If all the relevant bits are set, it might be in the set
        return True


# Test
bloom_filter = BloomFilter()
bloom_filter.add('apple')
print(bloom_filter.check('apple'))  # True
# False (or occasionally True due to false positives)
print(bloom_filter.check('orange'))

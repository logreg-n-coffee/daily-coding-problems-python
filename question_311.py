# Given a array that's sorted but rotated at some unknown pivot,
# in which all elements are distinct, find a "peak" element in O(log N) time.

# An element is considered a peak if it is greater than both its left and right neighbors.
# It is guaranteed that the first and last elements are lower than all others.

import unittest


def peak(array):
    n = len(array)
    start, end = 0, n - 1

    while start <= end:
        mid = (start + end) // 2

        # Checking if mid itself is a peak
        if (mid == 0 or array[mid] > array[mid - 1]) and \
           (mid == n - 1 or array[mid] > array[mid + 1]):
            return array[mid]

        # Decide the searching direction
        # If the array is rotated and we are in the "rotated" part,
        # the peak must be in the left half.
        elif mid > 0 and array[mid] < array[mid - 1]:
            end = mid - 1

        # Otherwise, go to the right half.
        else:
            start = mid + 1

    return -1  # This line will never be reached based on problem constraints


class TestPeak(unittest.TestCase):

    def test_small_array(self):
        # Only one valid peak is 4
        self.assertEqual(peak([1, 4, 2]), 4)

    def test_larger_array(self):
        # Peak can be 6 or 9
        self.assertEqual(peak([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]), 6)

        # Peak can be 8 or 10
        self.assertEqual(peak([4, 5, 6, 8, 10, 6, 5, 2, 1]), 10)

    def test_rotation(self):
        # Peak can be 6
        self.assertEqual(peak([4, 5, 6, 2, 1]), 6)

    def test_peak_condition(self):
        # Only one valid peak is 8
        array = [1, 4, 6, 8, 6, 4, 1]
        result = peak(array)
        self.assertEqual(result, 8)

        # Peak can be 5 or 6
        array = [1, 2, 3, 5, 3, 6, 4, 2, 1]
        result = peak(array)
        self.assertTrue(result in [5, 6])


if __name__ == "__main__":
    unittest.main()

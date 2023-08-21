# You are given a list of N numbers, in which each number is located at most k places away from its sorted position.
# For example, if k = 1, a given element at index 4 might end up at indices 3, 4, or 5.

# Come up with an algorithm that sorts this list in O(N log k) time.

# Intution: The problem can be efficiently tackled using a min heap. The key insight is that:
# given any number at index i in the array, its correct position in the sorted array will be in the range [i - k, i + k].
# This implies that the smallest number in this range will be the one that is supposed to be at index i in the sorted array.

# We can use a min heap of size k + 1 to always keep track of the smallest number in the next k + 1 numbers, as we iterate through the list.

# Algorithm:

# 1. Create a min heap and insert the first k + 1 elements into the heap.
# 2. For i = 0 to N - 1:
#   a. Extract the minimum from the heap and set it to the ith position in the array.
#   b. Insert the next element from the list into the heap, if there are any left.
# Now the array is sorted.

import heapq


def sort_k(nums, k):
    # create a min heap
    min_heap = []
    n = len(nums)

    # build the min heap - push first k + 1 elements into the heap
    for i in range(min(n, k + 1)):
        heapq.heappush(min_heap, nums[i])

    # for every element in the array
    for i in range(n):
        # place the smallest element (root) at the i-th position
        nums[i] = heapq.heappop(min_heap)

        # push the next element into the heap, if any
        if i + k + 1 < n:
            heapq.heappush(min_heap, nums[i + k + 1])

    return nums


# Driver code
if __name__ == "__main__":
    nums = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
    k = 2
    print(sort_k(nums, k))

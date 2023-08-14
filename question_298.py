# A girl is walking along an apple orchard with a bag in each hand.
# She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.

# Given an input describing the types of apples she will pass on her path,

# in order, determine the length of the longest portion of her path that consists of just two types of apple trees.

# For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3 (sequence is [3, 1, 1, 3]), with a length of four.


def longest_two_types(apples):
    start = 0
    max_length = 0
    freq_map: dict[int, int] = {}

    for end in range(len(apples)):
        freq_map[apples[end]] = freq_map.get(apples[end], 0) + 1

        while len(freq_map) > 2:
            freq_map[apples[start]] -= 1
            if freq_map[apples[start]] == 0:
                del freq_map[apples[start]]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length


# Test the function with the given example
test_apples = [2, 1, 2, 3, 3, 1, 3, 5]
print(longest_two_types(test_apples))

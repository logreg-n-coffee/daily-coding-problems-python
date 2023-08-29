# There are M people sitting in a row of N seats, where M < N.
# Your task is to redistribute people such that there are no gaps between any of them,
# while keeping overall movement to a minimum.

# For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1],

# where 0 represents an empty seat and 1 represents a person. In this case, one solution
# would be to place the person on the right in the fourth seat.

# We can consider the cost of a solution to be the sum of the absolute distance each person must move,
# so that the cost here would be 5.

# Given an input such as the one above,
# return the lowest possible cost of moving people to remove all gaps.

# -----
# Intuition: we can use a greedy approach. We want to minimize the overall movement while removing all the gaps between the people.
# One way to achieve this is by moving people closer to the median position of all the people.
# This is because the sum of the absolute differences is minimized when the numbers are adjusted around the median.

# Algo: Identify the positions where people are sitting and store them in a list.
# Calculate the new positions for the people if they were sitting together without any gaps.
# Calculate the cost by summing the absolute differences between the current and new positions for each person.


def min_cost_to_remove_gaps(seats: list[int]) -> int:
    # Step 1: Find the positions of all people (1s in the list)
    people_positions = [i for i, x in enumerate(seats) if x == 1]

    # Step 2: Calculate the median position
    median_index = len(people_positions) // 2
    median_position = people_positions[median_index]

    # Step 3: Calculate the new ideal positions for people around the median
    ideal_positions = [median_position + i -
                       median_index for i in range(len(people_positions))]

    # Step 4: Calculate the cost (sum of absolute differences between current and new positions)
    cost = sum(abs(a - b) for a, b in zip(people_positions, ideal_positions))

    return cost


# Test the function
test_input = [0, 1, 1, 0, 1, 0, 0, 0, 1]
print(min_cost_to_remove_gaps(test_input))

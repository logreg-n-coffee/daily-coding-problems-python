# You are given an array of length N, where each element i (i-th element) represents the number of ways we can produce i units of change.
# For example, [1, 0, 1, 1, 2] would indicate that there is only one way to make 0, 2, or 3 units,
# and two ways of making 4 units.

# Given such an array, determine the denominations that must be in use.

# In the case above, for example, there must be coins with value 2, 3, and 4.

# (index) 0 unit can be make in (value) 1 way
# (index) 1 unit can be make in (value) 0 way - no coin of denomination 1 is available
# (index) 2 unit can be make in (value) 1 way
# (index) 3 unit can be make in (value) 1 way
# (index) 4 unit can be make in (value) 2 ways, 2, 2 and 4

def find_denominations(ways):
    N = len(ways)
    denominations = set()

    # We know that there's only 1 way to produce 0 units: with no coins at all
    if ways[0] != 1:
        return "Invalid array: There must be exactly one way to make 0 units"

    # We know there are no coins with value 1 because ways[1] is 0
    if ways[1] != 0:
        return "Invalid array: There must be zero ways to make 1 unit"

    for i in range(2, N):
        # Calculate the number of combinations that can be made
        # with the known denominations
        calculated_ways = 0
        for d in denominations:
            if i - d >= 0:
                calculated_ways += ways[i - d]

        # If the calculated ways and given ways do not match, a new denomination is found
        if calculated_ways != ways[i]:
            denominations.add(i)

    return sorted(list(denominations))


# Example
ways = [1, 0, 1, 1, 2]
print(find_denominations(ways))  # Output should be [2, 3, 4]

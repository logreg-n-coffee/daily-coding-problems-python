# Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.

# On the ith jump, you may move exactly i places to the left or right.

# Find a path with the fewest number of jumps required to get from 0 to N.

# Observation:
#
# On the first jump, you can move 1 place either left (-1) or right (+1).
# On the second jump, you can move 2 places either left (-2) or right (+2).
# On the third jump, you can move 3 places either left (-3) or right (+3).
# And so on...

# The goal is to find the fewest number of jumps to reach a given integer N.

# The first step is to find the minimum number of jumps required to get close to N. .
#
# The sum of the first k jumps can be calculated as: Sum = k(k+1)/2

# We need to find a k such that Sum ≥ ∣N∣. This will be the maximum number of jumps we can make. Once we find this k,
# we can then backtrack to figure out the sequence of jumps that will lead us to N.

def find_fewest_jumps(n):
    # initializer varianles
    k = 0
    total_sum = 0

    # find the minimum number of jumps required to get close to N
    while total_sum < abs(n):
        k += 1
        total_sum += k

    # initialize a list to store the sequence of jumps
    jumps: list[int] = []

    # backtrack to figure out the sequence of jumps that will lead us to N
    for i in range(k, 0, -1):
        if total_sum - i >= abs(n):
            # if we can reduce total_sum to get close to N, then move left
            total_sum -= i * 2
            jumps.append(-i)
        else:
            # move right
            jumps.append(i)
            total_sum -= i

    # if n is negative, invert the sequence of jumps
    if n < 0:
        jumps = [-x for x in jumps]

    return jumps


# Test the function
# The function returns [4, 3, 2, 1], which means that you can get to the integer 10 by making jumps of 4 places to the right,
# 3 places to the right, 2 places to the right, and finally 1 place to the right.
# In other words, the sequence of jumps is 4+3+2+1=10.

print(find_fewest_jumps(10))  # expected [4, 3, 2, 1]
print(find_fewest_jumps(-10))  # expected [-4, -3, -2, -1]

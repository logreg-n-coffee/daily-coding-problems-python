# Write a function that returns the bitwise AND of all integers between M and N, inclusive.

# Intuition: Essentially, we are interested in finding the common prefix of the binary representations of M and N
# because the other bits will eventually be zeroed out by the AND operation.

# We shift both M and N to the right until they are equal
# (i.e., until we've isolated their common prefix),
# and then shift the result back to the left the same number of steps.


def bitwise_and_between_m_n_linear_time(M, N):
    # Initialize the result to N (since it's the maximum number in the range)
    result = N

    # If M == N, the AND operation would simply yield M (or N, they are the same)
    if M == N:
        return M

    # Loop from M to N - 1 and perform bitwise AND with result
    for i in range(M, N):
        result &= i
        # If the result ever becomes zero, the final AND will also be zero
        # (anything AND zero is zero)
        if result == 0:
            return 0

    return result


def bitwise_and_between_m_n_logn_time(m, n):
    shift = 0

    # Isolate the common prefix by shifting both numbers to the right
    while m < n:
        m >>= 1
        n >>= 1
        shift += 1

    # Shift back to the left to form the final ANDed number
    return n << shift


# Test the function
print(bitwise_and_between_m_n_linear_time(5, 7))  # Output should be 4
print(bitwise_and_between_m_n_linear_time(10, 15))  # Output should be 8
print(bitwise_and_between_m_n_linear_time(13, 15))  # Output should be 12

print(bitwise_and_between_m_n_logn_time(5, 7))  # Output should be 4
print(bitwise_and_between_m_n_logn_time(10, 15))  # Output should be 8
print(bitwise_and_between_m_n_logn_time(13, 15))  # Output should be 12

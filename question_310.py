# Write an algorithm that finds the total number of set bits in all integers between 1 and N.

def count_set_bits(n):
    return bin(n).count('1')


def total_set_bits_n_squared(n):
    total = 0

    for i in range(1, n + 1):
        total += count_set_bits(i)

    return total

# To see if we can do better, let us examine the binary representations of the first few integers.

# N  | binary
# ------------
# 0  | 000
# 1  | 001
# 2  | 010
# 3  | 011
# 4  | 100
# 5  | 101
# If we divide these numbers into even and odd sets, we end up with two groups, as follows:

# Even | Odd
# ------------
# 000  | 001
# 010  | 011
# 100  | 101
# Note that the two columns only differ in their last column, with even numbers having zeroes and odd numbers having ones. If there are an equal amount of even and odd numbers, which will happen if N is odd, this column will contribute a number of set bits equivalent to (N + 1) // 2. For example, here N == 5, so there are three numbers in each group, and each of the odd integers has a one in the last column.

# Furthermore, if we cut off this last column, the prefixes are the same in each group, and represent exactly the numbers between 0 and N // 2.

# Therefore, for an odd number N, we can form a recursive relationship for the number of set bits up to N:

# f(N) = (N + 1) / 2 + 2 * f(N / 2)
# Finally, in the case of an even number, we can simply count the set bits for that number, add it to our total, and solve for N - 1.


def total_set_bits_logn_squared(n) -> int:
    if n == 0:
        return 0
    elif n % 2 == 0:
        return count_set_bits(n) + total_set_bits_logn_squared(n - 1)
    elif n % 2 == 1:
        return (n + 1) // 2 + 2 * total_set_bits_logn_squared(n // 2)
    return 0  # default return val
